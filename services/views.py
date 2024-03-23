from django.views.generic import ListView, DetailView, TemplateView

from .models import Services
from sitesetting.models import Sites, AboutCompany, KeywordDiscription
from . import app_settings


class Hrm(TemplateView):
    """views"""

    template_name = "services/HRM." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "HRM",
    }


class StaticSites(TemplateView):
    """views"""

    template_name = "services/static_sites." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "Static Sites",
    }


class Portfollio(TemplateView):
    """views"""

    template_name = "services/portfollio." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "Portfollio",
    }


class Blogs(TemplateView):
    """views"""

    template_name = "services/blogs." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "Blogs",
    }


class PersonalSites(TemplateView):
    """views"""

    template_name = "services/personal_site." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "Personal Sites",
    }


class Ecommerce(TemplateView):

    """View"""

    template_name = "services/ecommerce." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "E-commerce",
    }


class MobileApp(TemplateView):

    """View"""

    template_name = "services/mobile_web_app." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "Mobile Web App",
    }


class Cms(TemplateView):

    """View"""

    template_name = "services/CMS." + app_settings.TEMPLATE_EXTENSION
    extra_context = {
        "app_data": Sites.objects.all(),
        "company_data": AboutCompany.objects.all(),
        "key": KeywordDiscription.objects.all(),
        "page_title": "CMS",
    }


class ServicesListViews(ListView):
    model = Services
    context_object_name = "service_list"
    template_name = "services/service_list." + app_settings.TEMPLATE_EXTENSION


class ServicesDetailViews(DetailView):
    model = Services
    context_object_name = "service"  # new
    template_name = "services/service_details." + app_settings.TEMPLATE_EXTENSION
