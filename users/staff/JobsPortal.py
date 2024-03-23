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

# local import
from users.staff import app_settings
from sitesetting.models import Sites
from pages.models import JobPortal
from pages.form import JobPortalForm, DateForm
from users.staff.utils import render_to_pdf

# date time
import datetime

# 3rd party
import csv


# @login_required(login_url=settings.LOGIN_URL)
# @user_passes_test(email_check)
# def BrandExportCsv(request):
#     """Brand Export CSV"""

#     response = HttpResponse(content_type="text/csv")
#     response["Content-Disposition"] = 'attachment; filename="brands.csv"'
#     brand = Brands.objects.all()
#     writer = csv.writer(response)
#     for b in brand:
#         writer.writerow(
#             [
#                 b.name,
#                 b.pic,
#             ]
#         )
#     return response


# @login_required(login_url=settings.LOGIN_URL)
# @user_passes_test(email_check)
# def BrandExportPdfAll(request):
#     """Staff Slider Export Pdf ALL"""
#     template_name = (
#         "staff/dashboard/brand/reports/export_pdfall." + app_settings.TEMPLATE_EXTENSION
#     )
#     pdf_name = "brand_list.pdf"
#     context = {
#         "app_data": Sites.objects.all(),
#         "brand": Brands.objects.all(),
#         "time": datetime.date.today(),
#         "doc_name": "Brand_list",
#     }
#     return render_to_pdf(template_name, context, pdf_name)


class JobDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):
    """DeleteView"""

    template_name = "staff/dashboard/Job_Portal/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = JobPortal
    context_object_name = "delete"
    success_url = reverse_lazy("job_list")
    success_message = "Item Deleted Successfully !"


class JobUpdate(
    StaffRequiredMixin, TestMixinUserEmail, SuccessMessageMixin, UpdateView
):
    """UpadteView"""

    template_name = (
        "staff/dashboard/Job_Portal/update." + app_settings.TEMPLATE_EXTENSION
    )
    login_url = reverse_lazy("account_login")
    model = JobPortal
    success_url = reverse_lazy("job_list")
    success_message = "Updated !"
    form_class = JobPortalForm
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Job Portal",
        "page_titel": app_settings.PAGE_TITLE,
    }


class JobDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """DetailView"""

    model = JobPortal
    login_url = reverse_lazy("account_login")
    context_object_name = "jobs"
    template_name = (
        "staff/dashboard/Job_Portal/detail." + app_settings.TEMPLATE_EXTENSION
    )
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Job Detail",
        "page_titel": app_settings.PAGE_TITLE,
    }


class JobCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):
    """createView"""

    template_name = (
        "staff/dashboard/Job_Portal/create." + app_settings.TEMPLATE_EXTENSION
    )
    login_url = reverse_lazy("account_login")
    model = JobPortal
    form_class = JobPortalForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        contex = {
            "form": form,
            "pagename": "Create Jobs",
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
        messages.success(self.request, "Created Successfully!")
        return reverse("job_list")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        errors = form.errors
        context = {
            "form": form,
            "pagename": "Create Jobs",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
            "errors": errors,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)


class JobsList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Views"""

    login_url = reverse_lazy("account_login")
    form_class = DateForm
    model = JobPortal
    template_name = "staff/dashboard/Job_Portal/list." + app_settings.TEMPLATE_EXTENSION

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        contex = {
            "form": form,
            "jobs": self.model.objects.all(),
            "pagename": "Jobs List",
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
        context = {
            "jobs": self.model.objects.all().filter(created_at__gte=fromdate),
            "form": form,
            "app_data": Sites.objects.all(),
            "pagename": "Job list",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }
        if fromdate:
            return render(self.request, self.template_name, context)
        if enddate:
            context = {
                "jobs": self.model.objects.all().filter(created_at__lte=enddate),
                "form": form,
                "pagename": app_settings.PAGE_NAME,
                "app_data": Sites.objects.all(),
                "page_title": app_settings.PAGE_TITLE,
            }
            return render(request, self.template_name, context)

    def form_invalid(self, form):
        return render(
            request,
            self.template_name,
            {
                "jobs": self.model.objects.all(),
                "form": form,
            },
        )
