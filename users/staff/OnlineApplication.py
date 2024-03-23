import time
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# redirects Imports
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# msg mixin import
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# template loader
from django.template import loader

# date  import
import datetime

# Generic Views Imports
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from users.mixins import (
    TestMixinUserEmail,
    TestMixinUserName,
    StaffRequiredMixin,
    email_check,
)
from django.contrib.auth.decorators import user_passes_test

# local Imports
from sitesetting.models import Sites
from sitesetting.form import DateForm
from pages.models import OnlineApplication
from pages.form import OnlineApplicationForm
from users.staff import app_settings
from datetime import date

# 3RD Party
# for pdf export
from users.staff.utils import render_to_pdf

# for csv export
import csv

# QR CODE
import io
import qrcode


# @login_required(login_url=settings.LOGIN_URL)
# @user_passes_test(email_check)
# def OnlineApplicationExportCsv(request):
#     """Online Requests Export CSV"""
#     login_url = reverse_lazy("account_login")
#     response = HttpResponse(content_type="text/csv")
#     response["Content-Disposition"] = 'attachment; filename="OnlineApplication.csv"'
#     OnlineApplication = OnlineApplication.objects.all()
#     writer = csv.writer(response)
#     for r in OnlineApplication:
#         writer.writerow(
#             [
#                 "Name",
#                 "Mobile",
#                 "Email",
#                 "Device Name",
#                 "Device Problem",
#                 "Created Date",
#             ]
#         )
#         writer.writerow(
#             [
#                 r.name,
#                 r.mobile,
#                 r.email,
#                 r.device_name,
#                 r.device_problem,
#                 r.created_at,
#             ]
#         )
#     return response


def qr_generate(data, size, version, border):
    qr = qrcode.QRCode(
        version=version,  # QR code version a.k.a size, None == automatic
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # lots of error correction
        box_size=size,  # size of each 'pixel' of the QR code
        border=border,  # minimum size according to spec
    )
    qr.add_data(data)
    img = qr.make_image()
    img_name = "qr" + str(time.time()) + ".png"
    img.save(settings.MEDIA_ROOT + "/" + img_name)

    return img_name


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def OnlineRequetsExportPdfbyId(request, pk):
    """Staff Online Request Export Pdf by id"""
    login_url = reverse_lazy("account_login")
    template_name = (
        "staff/dashboard/online_application/reports/export_pdfbyid."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = f'"{pk}"_online_application.pdf'
    online_application = OnlineApplication.objects.filter(id__gte=pk)
    # for QR COde
    size = 2
    version = 2
    border = 0
    for data in online_application:
        name = data.name
        application_no = data.application_no
        email = data.email
        mobile = data.mobile
        current_company = data.current_company
        current_salary = data.current_salary
        expected_salary = data.expected_salary
        expected_salary = data.expected_salary
        exprience = data.exprience
        skills = data.skills
        project_done = data.project_done
        awards = data.awards
        photo = data.photo
        sign = data.sign
        address = data.address
        created = data.created_at
        # QR CODE GEN
        qr_data = {
            "Name": data.name,
            "Email": data.email,
            "Mobile": data.mobile,
            "Applicatio No": data.application_no,
        }
        img_name = qr_generate(qr_data, size, version, border)
        pdf_name = f'"{data.name}"_online_application.pdf'
        context = {
            "app_data": Sites.objects.all(),
            "application_no": application_no,
            "name": name,
            "email": email,
            "mobile": mobile,
            "current_company": data.current_company,
            "current_salary": data.current_salary,
            "expected_salary": data.expected_salary,
            "expected_salary": data.expected_salary,
            "exprience": data.exprience,
            "skills": data.skills,
            "project_done": data.project_done,
            "awards": data.awards,
            "photo": data.photo,
            "sign": data.sign,
            "address": data.address,
            "created": created,
            "time": datetime.date.today(),
            "doc_name": "Application Form",
            "img_name": img_name,
        }
        return render_to_pdf(template_name, context, pdf_name)


# @login_required(login_url=settings.LOGIN_URL)
# @user_passes_test(email_check)
# def OnlineRequetsExportPdfbyDate(request):
#     """Staff OnlineApplication Export Pdf by DATE"""
#     login_url = reverse_lazy("account_login")
#     template_name = (
#         "staff/dashboard/online_application/reports/export_pdf_bydate."
#         + app_settings.TEMPLATE_EXTENSION
#     )
#     pdf_name = "online_request_filtered_list.pdf"

#     if request.method == "POST":
#         fromdate = request.POST.get("startdate")
#         enddate = request.POST.get("enddate")
#         data = Resume.objects.all().filter(
#             created_at__gte=fromdate, created_at__lte=enddate
#         )
#         context = {
#             "app_data": Sites.objects.all(),
#             "OnlineApplication": data,
#             "time": datetime.date.today(),
#             "doc_name": "Online Requests",
#         }
#         return render_to_pdf(template_name, context, pdf_name)

#     else:
#         context = {
#             "app_data": Sites.objects.all(),
#             "OnlineApplication": Resume.objects.all(),
#             "time": datetime.date.today(),
#             "doc_name": "Online Requests",
#         }
#         return render_to_pdf(template_name, context, pdf_name)


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def OnlineApplicationExportPdfAll(request):
    """Export Pdf ALL"""
    template_name = (
        "staff/dashboard/online_application/reports/export_pdfall."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = "online_application_list.pdf"
    context = {
        "app_data": Sites.objects.all(),
        "online_application": OnlineApplication.objects.all(),
        "time": datetime.date.today(),
        "doc_name": "Online Application List",
    }
    return render_to_pdf(template_name, context, pdf_name)


class OnlineApplicationDetails(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """DetailView"""

    model = OnlineApplication
    login_url = reverse_lazy("account_login")
    context_object_name = "online_application"
    template_name = (
        "staff/dashboard/online_application/detail." + app_settings.TEMPLATE_EXTENSION
    )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        data = "www.fixenix.com"
        img = qrcode.make(data, box_size=2)
        img_name = "qr" + str(time.time()) + ".png"
        img.save(settings.MEDIA_ROOT + "/QR/" + img_name)
        # Add in a QuerySet of all the books
        context["app_data"] = Sites.objects.all()
        context["pagename"] = "Online Application List"
        context["doc_name"] = "Online Application List"
        context["date"] = datetime.date.today()
        context["qr_code_img"] = img_name
        return context


class OnlineApplicationList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Views By date"""

    login_url = reverse_lazy("account_login")
    form_class = DateForm
    model = OnlineApplication
    template_name = (
        "staff/dashboard/online_application/list." + app_settings.TEMPLATE_EXTENSION
    )

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        contex = {
            "form": form,
            "online_application": self.model.objects.all(),
            "pagename": "Online Application List",
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
            "online_application": self.model.objects.all().filter(
                created_at__gte=fromdate
            ),
            "form": form,
            "app_data": Sites.objects.all(),
            "pagename": "Brand list",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }
        if fromdate:
            return render(self.request, self.template_name, context)
        if enddate:
            context = {
                "online_application": self.model.objects.all().filter(
                    created_at__lte=enddate
                ),
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
                "online_application": self.model.objects.all(),
                "form": form,
            },
        )
