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
from users.staff import app_settings
from sitesetting.models import Sites, GoogleFeeds
from sitesetting.form import GfForm


class GfDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):

    """DeleteView"""

    template_name = "staff/dashboard/gf/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = GoogleFeeds
    context_object_name = "delete"
    success_url = reverse_lazy("gf_list")
    success_message = "Deleted Successfully !"


class GfUpdate(StaffRequiredMixin, TestMixinUserEmail, UpdateView):
    """UpdateView"""

    template_name = "staff/dashboard/gf/update." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = GoogleFeeds
    success_url = reverse_lazy("gf_list")
    success_message = "Updated Successfully !"
    form_class = GfForm
    context_object_name = "gf"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Google Feeds",
        "page_title": app_settings.PAGE_TITLE,
    }


class GfDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """DetailView"""

    template_name = "staff/dashboard/gf/detail." + app_settings.TEMPLATE_EXTENSION
    model = GoogleFeeds
    login_url = reverse_lazy("account_login")
    context_object_name = "gf"
    extra_context = {"app_data": Sites.objects.all(), "pagename": "Google Feeds"}


class GfCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):
    """create"""

    template_name = "staff/dashboard/gf/create." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = GoogleFeeds
    form_class = GfForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "app_data": Sites.objects.all(),
                "pagename": "Google Feed Create",
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Added Successfully ! ")
        return reverse("gf_list")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return render(request, self.template_name, {"form": form})


class GfList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """ListView"""

    template_name = "staff/dashboard/gf/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = GoogleFeeds
    context_object_name = "gf"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Google Feeds",
        "page_title": app_settings.PAGE_TITLE,
    }
