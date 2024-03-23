from django.forms import ModelForm
from django import forms
from .models import (
    SliderData,
    Sites,
    KeywordDiscription,
    Features,
    AboutCompany,
    Faq,
    OurClients,
    GoogleFeeds,
    Brands,
)
from django.forms import TextInput, FileInput, EmailInput,DateInput


class BrandForm(ModelForm):
    """brand form"""

    class Meta:
        model = Brands
        fields = ["name", "pic"]


class GfForm(ModelForm):
    """Google Feed form"""

    class Meta:
        model = GoogleFeeds
        fields = "__all__"


class OcForm(ModelForm):
    """our clients form"""

    class Meta:
        model = OurClients
        fields = "__all__"


class FaqForm(ModelForm):
    """faq form"""

    class Meta:
        model = Faq
        fields = "__all__"


class AboutCompanyForm(ModelForm):
    """About Comapny"""

    class Meta:
        model = AboutCompany
        fields = ["about_company"]


class FeaturesForm(ModelForm):
    """Features form"""

    class Meta:
        model = Features
        fields = "__all__"


class KeywordDiscriptionForm(ModelForm):
    """Keyword forms"""

    class Meta:
        model = KeywordDiscription
        fields = [
            "keyword",
            "discription",
        ]


class StaffSitesForm(ModelForm):

    """sites setting form"""

    class Meta:
        model = Sites

        fields = [
            "display_name",
            "domain_name",
            "app_email",
            "app_mobile",
            "app_address",
            "app_version",
            "app_logo",
            "app_fevicon",
            "app_stamp",
        ]

        widgets = {
            "display_name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "display_name",
                }
            ),
            "domain_name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "domain name",
                }
            ),
            "app_email": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app email",
                    "type": "email",
                }
            ),
            "app_mobile": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app mobile",
                }
            ),
            "app_address": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app address",
                }
            ),
            "app_version": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app version",
                }
            ),
            "app_logo": FileInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "type": "file",
                }
            ),
        }


class SliderCreateForm(ModelForm):
    """slider creation form"""

    class Meta:
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


class DateForm(forms.Form):
    """date filter"""

    startdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "label": "From",
                "class": "form-control",
                "type": "date",
                "style": "width: 200px;",
            }
        )
    )
    enddate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "label": "From",
                "class": "form-control",
                "type": "date",
                "style": "width: 200px;",
            }
        )
    )
