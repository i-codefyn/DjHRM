# time
from django.utils import timezone

# revers and redirect
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# validation
from django.core.exceptions import ValidationError

# random number
import random
import uuid

# requests
import requests
import re

# settingd imports
from django.conf import settings
from . import app_setting

# mail
from django.core.mail import EmailMultiAlternatives  # form html send
from django.core.mail import send_mail

# template rendering
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# jason response
from django.http import JsonResponse

# appp imports views
from django.views.generic import TemplateView, CreateView, View, FormView, ListView
from django.views.generic.detail import SingleObjectMixin
from sitesetting.models import (
    Sites,
    Features,
    Faq,
    AboutCompany,
    KeywordDiscription,
)

# app import models
from .models import ContactUs, FeedBack, JobPortal, OnlineApplication

# app imoprt forms
from pages.form import (
    ContactForm,
    FeedBackForm,
    OtpVerifyForm,
    DateForm,
    OnlineApplicationForm,
    FileUploadForm,
)


def application_id():
    number = "CFYN" + (str(uuid.uuid4()).split("-")[1]).upper()
    return number


class HomePage(TemplateView):
    PAGE_TITLE = "Job Portal"
    template_name = "home/index." + app_setting.TEMPLATE_EXTENSION
    extra_context = {
        "page_tite": PAGE_TITLE,
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
    }


class JobPortal(ListView):
    """List Views"""

    PAGE_TITLE = "Job Portal"
    template_name = "home/job_portal." + app_setting.TEMPLATE_EXTENSION
    model = JobPortal
    context_object_name = "jobs"
    form_class = DateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        contex = {
            "form": form,
            "jobs": self.model.objects.all(),
            "page_tite": self.PAGE_TITLE,
            "app_data": Sites.objects.all(),
            "company_data": AboutCompany.objects.all(),
        }

        return render(request, self.template_name, contex)

    def post(self, request, *args, **kwargs):
        form = self.form_class
        if request.method == "POST":
            fromdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")
            jobs = self.model.objects.all()

            if fromdate:
                data1 = jobs.filter(created_at__gte=fromdate)
                context = {
                    "jobs": data1,
                    "form": form,
                    "app_data": Sites.objects.all(),
                    "pagename": self.page_name,
                    "page_title": app_settings.PAGE_TITLE,
                }
                return render(request, self.template_name, context)
            if enddate:
                data2 = jobs.filter(created_at__lte=enddate)
                context = {
                    "jobs": data2,
                    "form": form,
                    "app_data": Sites.objects.all(),
                    "pagename": self.page_name,
                    "page_title": app_settings.PAGE_TITLE,
                }
                return render(request, self.template_name, context)
        else:
            form = self.form_class
            context = {
                "jobs": self.model.objects.all(),
                "form": form,
            }
            return render(request, self.template_name, context)


class JobApply(View):
    """View"""

    template_name = "home/apply_form." + app_setting.TEMPLATE_EXTENSION
    model = OnlineApplication
    form_class = OnlineApplicationForm
    import random

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "app_data": Sites.objects.all(),
                "company_data": AboutCompany.objects.all(),
                "key": KeywordDiscription.objects.all(),
                "page_title": "Home Page",
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None, request.FILES or None)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, to_mail):
        messages.success(self.request, f"OTP is Sent to {to_mail}")
        return reverse_lazy("otp_verify")

    def form_valid(self, form):
        """if from data is valid"""

        if self.request.method == "POST":
            if form.is_valid():
                n = form.cleaned_data["name"]
                e = form.cleaned_data["email"]
                m = form.cleaned_data["mobile"]
                cc = form.cleaned_data["current_company"]
                cs = form.cleaned_data["current_salary"]
                es = form.cleaned_data["expected_salary"]
                ex = form.cleaned_data["exprience"]
                sk = form.cleaned_data["skills"]
                pd = form.cleaned_data["project_done"]
                aw = form.cleaned_data["awards"]
                aid = application_id()
                # file = form.cleaned_data["resume"]
                self.request.session["name"] = n
                self.request.session["email"] = e
                self.request.session["mobile"] = m
                self.request.session["current_company"] = cc
                self.request.session["current_salary"] = cs
                self.request.session["expected_salary"] = es
                self.request.session["exprience"] = ex
                self.request.session["skills"] = sk
                self.request.session["project_done"] = pd
                self.request.session["awards"] = aw
                self.request.session["application_no"] = aid
                # self.request.session["resume"] = file
                from_mail = settings.EMAIL_HOST_USER
                to_mail = e

                otp = randomDigits(4)
                expiry = get_expiry()
                self.request.session["otp"] = otp
                self.request.session["time"] = str(expiry)
                template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
                subject = "OTP for Final Submit"
                context = {
                    "title": "Email Verification Code",
                    "content": f"your OTP is {otp} .Dont share with anyone",
                }

                SendHTMLMail(subject, context, template_name, to_mail, from_mail)
                # self.request.session.set_expiry(100)
                return HttpResponseRedirect(self.get_success_url(to_mail))

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        context = {
            "form": form,
            "app_data": Sites.objects.all(),
            "company_data": AboutCompany.objects.all(),
            "key": KeywordDiscription.objects.all(),
            "page_title": "Home Page",
        }
        for error in errors:
            messages.error(self.request, f"Please Check {error}-& Try Again")
            return render(self.request, self.template_name, context)


def OtpReset(request):
    otp = randomDigits(4)
    expiry = get_expiry()
    request.session["otp"] = otp
    request.session["time"] = str(expiry)
    from_mail = settings.EMAIL_HOST_USER
    to_mail = request.session["email"]
    template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
    subject = "OTP for Final Submit"
    context = {
        "title": "OTP For Email Varifiaction",
        "content": f"your OTP is {otp} .Dont share with anyone",
    }
    SendHTMLMail(subject, context, template_name, to_mail, from_mail)
    message = f"OTP  has Send to Your {to_mail}"
    messages.success(request, message)
    return HttpResponseRedirect(reverse_lazy("otp_verify"))


class OtpVerify(View):
    form_class = OtpVerifyForm
    template_name = "home/otpverify." + app_setting.TEMPLATE_EXTENSION
    model = OnlineApplication

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        """otp submit"""
        a = form.cleaned_data["otp1"]
        b = form.cleaned_data["otp2"]
        c = form.cleaned_data["otp3"]
        d = form.cleaned_data["otp4"]
        list = [a, b, c, d]
        s = [str(i) for i in list]
        u_otp = int("".join(s))
        otp = self.request.session.get("otp")
        name = self.request.session["name"]
        # mobile = self.request.session.get("mobile")
        # current_company = self.request.session.get("current_company")
        # current_salary = self.request.session.get("current_salary")
        # expected_salary = self.request.session.get("expected_salary")
        # exprience = self.request.session.get("exprience")
        # skills = self.request.session.get("skills")
        # project_done = self.request.session.get("project_done")
        # awards = self.request.session.get("awards")
        # resume = self.request.session.get("resume")
        email_address = self.request.session.get("email")
        expriry = self.request.session.get("time")
        _now = str(timezone.now())
        if int(otp) == int(u_otp) and (_now < expriry):
            # Resume.objects.create(
            #     name=name,
            #     mobile=mobile,
            #     email=email_address,
            #     current_company=current_company,
            #     current_salary=current_salary,
            #     expected_salary=expected_salary,
            #     exprience=exprience,
            #     skills=skills,
            #     project_done=project_done,
            #     awards=awards,
            #     resume=resume,
            # )
            # self.request.session.delete("otp")
            # self.request.session.delete("name")
            # self.request.session.delete("email")
            # self.request.session.delete("mobile")
            # self.request.session.delete("current_company")
            # self.request.session.delete("current_salary")
            # self.request.session.delete("expected_salary")
            # self.request.session.delete("exprience")
            # self.request.session.delete("skills")
            # self.request.session.delete("project_done")
            # self.request.session.delete("awards")
            # self.request.session.delete("resume")
            # messages.success(self.request, "Request Successfully Submited ! Thank You")
            # return JsonResponse({"messages": "success"}, status=200)
            messages.info(self.request, "Upload Resume Here")
            return HttpResponseRedirect(reverse_lazy("upload_file"))
        else:
            if _now > expriry:
                error = "Otp Expired ! Try Again"
                messages.error(self.request, error)
                return JsonResponse({"errors": error}, status=400)

            error = f"Please Put Valid OTP "
            messages.error(self.request, error)
            return JsonResponse({"errors": error}, status=400)

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        for error in errors:
            return JsonResponse({"errors": error}, status=400)


class UploadFile(View):
    template_name = "home/file_upload." + app_setting.TEMPLATE_EXTENSION
    form_class = FileUploadForm
    model = OnlineApplication

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None, request.FILES or None)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """

        name = self.request.session["name"]
        mobile = self.request.session.get("mobile")
        current_company = self.request.session.get("current_company")
        current_salary = self.request.session.get("current_salary")
        expected_salary = self.request.session.get("expected_salary")
        exprience = self.request.session.get("exprience")
        skills = self.request.session.get("skills")
        project_done = self.request.session.get("project_done")
        awards = self.request.session.get("awards")
        resume = self.request.FILES["resume"]
        photo = self.request.FILES["photo"]
        sign = self.request.FILES["sign"]
        email_address = self.request.session.get("email")
        application_no = self.request.session.get("application_no")
        expriry = self.request.session.get("time")
        try:
            OnlineApplication.objects.create(
                application_no=application_no,
                name=name,
                mobile=mobile,
                email=email_address,
                current_company=current_company,
                current_salary=current_salary,
                expected_salary=expected_salary,
                exprience=exprience,
                skills=skills,
                project_done=project_done,
                awards=awards,
                resume=resume,
                photo=photo,
                sign=sign,
            )
            from_mail = settings.EMAIL_HOST_USER
            to_mail = email_address
            template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
            subject = "Submmited Successfully"
            context = {
                "title": "Form Submmited Successfully",
                "content": f"Dear {name}:Your Application Id is:{application_no}",
            }
            SendHTMLMail(subject, context, template_name, to_mail, from_mail)
            self.request.session.delete("otp")
            self.request.session.delete("name")
            self.request.session.delete("email")
            self.request.session.delete("mobile")
            self.request.session.delete("current_company")
            self.request.session.delete("current_salary")
            self.request.session.delete("expected_salary")
            self.request.session.delete("exprience")
            self.request.session.delete("skills")
            self.request.session.delete("project_done")
            self.request.session.delete("awards")
            self.request.session.delete("application_no")
            messages.success(self.request, f"Application No:{application_no}")
            return HttpResponseRedirect(reverse_lazy("apply_link"))
        except:
            message = "Invalid Data"
            messages.error(self.request, message)
            return render(request, self.template_name, {"form": form})

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        for error in errors:
            message = "Invalid Data"
            messages.error(self.request, message)
            return render(self.request, self.template_name, {"form": form})


class ContactFormView(View):
    template_name = "home/contact_us." + app_setting.TEMPLATE_EXTENSION
    form_class = ContactForm
    PAGE_TITLE = "Contact Page"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        contex = {
            "form_contact": form,
            "app_data": Sites.objects.all(),
            "company_data": AboutCompany.objects.all(),
            "key": KeywordDiscription.objects.all(),
            "page_title": "Contact_Us",
        }

        return render(request, self.template_name, contex)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Thank You For Writting Us !")
        return reverse("contactus")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        form.save()
        context = {
            "title": "Thank you for Writting Us!",
            "content": "Thank you for your feedback !",
        }
        from_mail = settings.EMAIL_HOST_USER
        template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
        to_mail = email
        subject = "Thank you for Writting Us!"
        SendHTMLMail(subject, context, template_name, to_mail, from_mail)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        context = {
            "form_contact": form,
            "app_data": Sites.objects.all(),
            "company_data": AboutCompany.objects.all(),
            "key": KeywordDiscription.objects.all(),
            "page_title": "Contact_Us",
            "errors": errors,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)


class FeedBackFormView(FormView):
    template_name = "home/feedback." + app_setting.TEMPLATE_EXTENSION
    form_class = FeedBackForm
    PAGE_TITLE = "Feedback"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

    def get_context_data(self, **kwargs):
        context = super(FeedBackFormView, self).get_context_data(**kwargs)
        context["app_data"] = Sites.objects.all()
        context["company_data"] = AboutCompany.objects.all()
        context["key"] = KeywordDiscription.objects.all()
        context["faq"] = Faq.objects.all()
        return context

    def get_success_url(self):
        return reverse("feedback")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        email = form.cleaned_data["email"]
        form.save(commit=False)
        context = {"title": "Feedback", "content": "Thank you for your feedback !"}
        from_mail = settings.EMAIL_HOST_USER
        template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
        to_mail = email
        subject = "Thank you for Feedback!"
        SendHTMLMail(subject, context, template_name, to_mail, from_mail)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        errors = form.errors
        for error in errors:
            return JsonResponse({"errors": error}, status=400)


class OurWorks(TemplateView):
    PAGE_TITLE = "Our Works"
    template_name = "home/works." + app_setting.TEMPLATE_EXTENSION
    extra_context = {
        "page_tite": PAGE_TITLE,
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
    }


class AboutUs(TemplateView):
    PAGE_TITLE = "Home Page"
    template_name = "home/about_us." + app_setting.TEMPLATE_EXTENSION
    extra_context = {
        "page_tite": PAGE_TITLE,
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
    }


def SendMail(SenderMail, message, RecieverEmail):
    subject = (f"Thank You For Writting Us!",)
    message = message
    from_email = SenderMail
    recipient_list = [RecieverEmail]
    return send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


def SendOtp(email, message, e):
    subject = ("Otp",)
    message = message
    from_email = email
    recipient_list = [e]
    return send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


class DisclamerView(TemplateView):
    template_name = "home/Disclamer." + app_setting.TEMPLATE_EXTENSION
    extra_context = {"page_title": "disclamer"}


class TermsAndConditionsView(TemplateView):
    """
    Terms And Conditions
    """

    template_name = "home/terms_conditions." + app_setting.TEMPLATE_EXTENSION
    extra_context = {"page_title": "Terms & Conditions"}


class FaqsView(ListView):
    """FAQs Views"""

    PAGE_TITLE = "FAQs"
    template_name = "home/faqs." + app_setting.TEMPLATE_EXTENSION
    # paginate_by = 100  # if pagination is desired
    model = Faq
    context_object_name = "faq"
    extra_context = {
        "page_tite": PAGE_TITLE,
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
    }


def SendHTMLMail(subject, context, template_name, to_mail, from_mail):
    """Html Send Through Email"""
    context = context
    subject = subject
    html_content = render_to_string(template_name, context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_mail, [to_mail])
    email.attach_alternative(html_content, "text/html")
    return email.send()


def randomDigits(digits):
    lower = 10 ** (digits - 1)
    upper = 10**digits - 1
    at = random.randint(lower, upper)
    return at


def get_expiry():
    now = timezone.now()
    expiry_seconds = 120
    expiry_time = timezone.timedelta(seconds=expiry_seconds)
    expiry = now + expiry_time
    return expiry
