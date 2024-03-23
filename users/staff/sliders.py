from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# redirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

# generic import
from django.views.generic import (
    CreateView,
    DeleteView,
    View,
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
)
from users.mixins import (
    TestMixinUserEmail,
    TestMixinUserName,
    StaffRequiredMixin,
    email_check,
)
from django.contrib.auth.decorators import user_passes_test

# alert Msg
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# date time
import datetime

# template loader
from django.template import loader

# 3RD Party
import csv

# LOCAL
from users.staff.utils import render_to_pdf
from users.staff import app_settings
from sitesetting.form import DateForm
from users.models import CustomUser
from sitesetting.models import SliderData, Sites
from sitesetting.form import SliderCreateForm


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def SliderExportCsv(request):
    """Slider Export CSV"""

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="sliderdata.csv"'
    slider = SliderData.objects.all()
    writer = csv.writer(response)
    for s in slider:
        writer.writerow(
            [
                s.heading1_title,
                s.heading1,
                s.heading2_title,
                s.heading2,
                s.heading3_title,
                s.heading3,
                s.heading4_title,
                s.heading4,
            ]
        )
    return response


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def SliderExportPdfbyId(request, pk):
    """Staff Slider Export Pdf by id"""
    template_name = (
        "staff/dashboard/slider/reports/export_pdfbyid."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = f'"{pk}"slider.pdf'
    context = {
        "app_data": Sites.objects.all(),
        "slider": SliderData.objects.filter(id__gte=pk),
        "time": datetime.date.today(),
        "doc_name": "slider List",
    }
    return render_to_pdf(template_name, context, pdf_name)


class SliderList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Staff Slider Views By date"""

    form_class = DateForm
    model = SliderData
    template_name = "staff/dashboard/slider/list." + app_settings.TEMPLATE_EXTENSION
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        contex = {
            "form": form,
            "slider": self.model.objects.all(),
            "pagename": app_settings.PAGE_NAME,
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }

        return render(request, self.template_name, contex)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if request.method == "POST":
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        fromdate = self.request.POST.get("startdate")
        enddate = self.request.POST.get("enddate")
        slider = self.model.objects.all()
        context = {
            "slider": slider.filter(created_at__gte=fromdate),
            "form": form,
            "app_data": Sites.objects.all(),
            "pagename": "slider_list",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }
        if fromdate:
            return render(self.request, self.template_name, context)
        if enddate:
            context = {
                "slider": slider.filter(created_at__lte=enddate),
                "form": form,
                "pagename": app_settings.PAGE_NAME,
                "app_data": Sites.objects.all(),
                "page_title": app_settings.PAGE_TITLE,
            }
            return render(request, self.template_name, context)

    def form_invalid(self, form):
        form = SliderCreateForm
        data = SliderData.objects.all()
        return render(
            request,
            self.template_name,
            {
                "slider": data,
                "form": form,
            },
        )


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def SliderExportPdfbyDate(request):
    """Staff Slider Export Pdf by DATE"""
    template_name = (
        "staff/dashboard/slider/reports/export_pdfall."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = "slider_list.pdf"

    if request.method == "POST":
        fromdate = request.POST.get("startdate")
        enddate = request.POST.get("enddate")
        context = {
            "app_data": Sites.objects.all(),
            "slider": SliderData.objects.all().filter(
                created_at__gte=fromdate, created_at__lte=enddate
            ),
            "time": datetime.date.today(),
            "doc_name": "slider List",
        }
        return render_to_pdf(template_name, context, pdf_name)
    else:
        context = {
            "app_data": Sites.objects.all(),
            "slider": SliderData.objects.all(),
            "time": datetime.date.today(),
            "doc_name": "slider List",
        }
        return render_to_pdf(template_name, context, pdf_name)


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def SliderExportPdfAll(request):
    """Staff Slider Export Pdf ALL"""
    template_name = (
        "staff/dashboard/slider/reports/export_pdfall."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = "slider_list.pdf"
    context = {
        "app_data": Sites.objects.all(),
        "slider": SliderData.objects.all(),
        "time": datetime.date.today(),
        "doc_name": "slider_list",
    }
    return render_to_pdf(template_name, context, pdf_name)


class SliderUpdate(StaffRequiredMixin, TestMixinUserEmail, UpdateView):

    """Staff Slider Update"""

    model = SliderData

    fields = [
        "heading1_title",
        "heading1",
        "bg1",
        "heading2_title",
        "heading2",
        "bg2",
        "heading3_title",
        "heading3",
        "bg3",
        "heading4_title",
        "heading4",
        "bg4",
    ]

    success_message = " Slider Successfully Updated!"
    context_object_name = "slider"
    success_url = reverse_lazy("slider_list")
    login_url = "account_login"
    template_name = "staff/dashboard/slider/update." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": app_settings.PAGE_NAME,
        "page_title": app_settings.PAGE_TITLE,
    }


class SliderDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):
    """Staff Slider Delete"""

    model = SliderData
    success_url = reverse_lazy("slider_list")
    template_name = "staff/dashboard/slider/delete." + app_settings.TEMPLATE_EXTENSION
    context_object_name = "delete"
    success_message = "Slider Deleted Successfully"


class SliderDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """Staff Slider Detail View"""

    model = SliderData
    context_object_name = "slider"
    template_name = "staff/dashboard/slider/detail." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("login")
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Slider Detail",
        "page_title": app_settings.PAGE_TITLE,
    }


class SliderCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):
    template_name = "staff/dashboard/slider/create." + app_settings.TEMPLATE_EXTENSION
    login_url = "account_login"
    context_object_name = "slider"
    form_class = SliderCreateForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        contex = {
            "form": form,
            "pagename": "Slider Create Form",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }

        return render(request, self.template_name, contex)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Thank You For Writting Us !")
        return reverse("slider_list")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        form.save()
        messages.success(self.request, "Slider Created Successfully")
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        errors = form.errors
        context = {
            "form": form,
            "pagename": app_settings.PAGE_NAME,
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
            "errors": errors,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)
