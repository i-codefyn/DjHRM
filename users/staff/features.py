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
from sitesetting.models import Features, Sites
from sitesetting.form import FeaturesForm


class FeaturesDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):
    """feature delete"""

    template_name = "staff/dashboard/features/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Features
    context_object_name = "delete"
    success_url = reverse_lazy("feature_list")
    success_message = "Deleted Successfully !"


class FeaturesCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):

    """feature create"""

    template_name = "staff/dashboard/features/create." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Features
    form_class = FeaturesForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(
            request,
            self.template_name,
            {"form": form, "app_data": Sites.objects.all(), "pagename": "Features"},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return form_valid(form)
        else:
            return form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Addedd Success Fully.")
        return reverse("feature_list")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return render(request, self.template_name, {"form": form})


class FeaturesUpdate(StaffRequiredMixin, TestMixinUserEmail, UpdateView):
    """feature upadte"""

    template_name = "staff/dashboard/features/update." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Features
    success_url = reverse_lazy("feature_list")
    success_message = "Features Updated !"
    form_class = FeaturesForm
    context_object_name = "features"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Features",
        "page_title": app_settings.PAGE_TITLE,
    }


class FeaturesDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """featues detail"""

    model = Features
    login_url = reverse_lazy("account_login")
    context_object_name = "f"
    template_name = "staff/dashboard/features/detail." + app_settings.TEMPLATE_EXTENSION
    context_object_name = "features"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Features",
        "page_title": app_settings.PAGE_TITLE,
    }


class FeaturesList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """features LISTVIEWS"""

    template_name = "staff/dashboard/features/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Features
    context_object_name = "features"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Features",
        "page_title": app_settings.PAGE_TITLE,
    }
