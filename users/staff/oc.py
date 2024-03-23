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
from sitesetting.models import Features, Sites, OurClients
from sitesetting.form import OcForm


class ClientDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):
    """DeleteView"""

    template_name = "staff/dashboard/oc/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = OurClients
    context_object_name = "delete"
    success_url = reverse_lazy("oc_list")
    success_message = "Deleted !"


class ClientUpdate(StaffRequiredMixin, TestMixinUserEmail, UpdateView):

    """UpdateView"""

    template_name = "staff/dashboard/oc/update." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = OurClients
    success_url = reverse_lazy("oc_list")
    success_message = "Updated Successfully !"
    form_class = OcForm
    context_object_name = "oc"
    extra_context = {"app_data": Sites.objects.all(), "pagename": "Our Clients Details"}


class ClientDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """DetailView"""

    template_name = "staff/dashboard/oc/detail." + app_settings.TEMPLATE_EXTENSION
    model = OurClients
    login_url = reverse_lazy("account_login")
    context_object_name = "oc"
    extra_context = {"app_data": Sites.objects.all(), "pagename": "Our Clients Details"}


class ClientCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):
    """create"""

    template_name = "staff/dashboard/oc/create." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = OurClients
    form_class = OcForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                "form_oc": form,
                "app_data": Sites.objects.all(),
                "pagename": "Oue Clients",
            },
        )

    def get_success_url(self):
        messages.success(self.request, "Created Successfully !")
        return reverse("oc_list")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return render(request, self.template_name, {"form_oc": form})


class ClientList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """ListView"""

    template_name = "staff/dashboard/oc/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = OurClients
    context_object_name = "oc"
    extra_context = {"app_data": Sites.objects.all(), "pagename": "Our Clients Details"}
