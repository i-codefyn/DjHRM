from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# alert msg
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# generic import
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView,
)
from users.mixins import (
    TestMixinUserEmail,
    TestMixinUserName,
    StaffRequiredMixin,
    email_check,
)
from django.contrib.auth.decorators import user_passes_test

# local  import
from sitesetting.models import Sites, KeywordDiscription
from sitesetting.form import KeywordDiscriptionForm
from users.staff import app_settings


class KeywordDiscriptionUpdate(StaffRequiredMixin, TestMixinUserEmail, UpdateView):
    """key update"""

    template_name = "staff/dashboard/keywords/update." + app_settings.TEMPLATE_EXTENSION
    model = KeywordDiscription
    context_object_name = "keys"
    fields = [
        "keyword",
        "discription",
    ]
    login_url = reverse_lazy("account_login")
    success_message = "updated Successfully !"
    extra_context = {
        "pagename": "Key & Discriptions",
        "app_data": Sites.objects.all(),
        "page_title": app_settings.PAGE_TITLE,
    }


class KeywordDiscriptionDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):
    """keyword delete view"""

    model = KeywordDiscription
    template_name = "staff/dashbaord/keywords/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    success_url = reverse_lazy("keywords_list")
    success_message = "Kyes & disc Deleted!"


class KeywordDiscriptionCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):
    """Keyword and dis add"""

    model = KeywordDiscription
    template_name = "staff/dashboard/keywords/create." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    form_class = KeywordDiscriptionForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "app_data": Sites.objects.all(),
                "pagename": "Keyword Create",
                "page_title": app_settings.PAGE_TITLE,
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Keys and Disc Addedd Successfully.")
        return reverse("keywords_list")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form})


class KeywordsDiscriptionsList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Keywords And Discriptions"""

    model = KeywordDiscription
    template_name = "staff/dashboard/keywords/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    context_object_name = "keys"
    extra_context = {
        "pagename": "Key and Disc",
        "app_data": Sites.objects.all(),
        "page_title": app_settings.PAGE_TITLE,
    }


class KeywordsDiscriptionsDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    template_name = "staff/dashboard/keywords/detail." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = KeywordDiscription
    context_object_name = "keys"
    extra_context = {
        "pahename ": "Key and Disc",
        "app_data": Sites.objects.all(),
        "page_title": app_settings.PAGE_TITLE,
    }
