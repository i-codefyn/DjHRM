from django.forms import ModelForm
from django import forms
from django.forms import (
    TextInput,
    FileInput,
    EmailInput,
    Textarea,
    NumberInput,
    DateInput,
)
from .models import ContactUs, FeedBack, OnlineApplication, JobPortal

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

import re

REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


class JobPortalForm(ModelForm):
    class Meta:
        model = JobPortal
        fields = [
            "post_name",
            "descriptions",
            "exprience",
            "salary",
            "apply_link",
            "last_date",
        ]

        widgets = {
            "post_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Post Name",
                    "id": "floatingInput",
                }
            ),
            "descriptions": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descriptions",
                    "id": "floatingInput",
                    "type": "textarea",
                }
            ),
            "exprience": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "exprience",
                    "id": "floatingInput",
                    "type": "number",
                }
            ),
            "salary": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "salary",
                    "id": "floatingInput",
                    "type": "number",
                }
            ),
            "apply_link": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "apply_link",
                    "id": "floatingInput",
                    "type": "text",
                }
            ),
            "last_date": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "apply_link",
                    "id": "floatingInput",
                    "type": "date",
                }
            ),
        }


class FileUploadForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = OnlineApplication
        fields = [
            "resume",
            "photo",
            "sign",
        ]
        widgets = {
            "resume": FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "resume",
                    "id": "floatingInput",
                }
            ),
            "photo": FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Photo",
                    "id": "floatingInput",
                }
            ),
            "sign": FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Sign",
                    "id": "floatingInput",
                }
            ),
        }


class OnlineApplicationForm(ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = OnlineApplication
        fields = [
            "name",
            "email",
            "mobile",
            "current_company",
            "current_salary",
            "expected_salary",
            "exprience",
            "skills",
            "project_done",
            "awards",
            "address",
        ]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px;  font-weight:500; ",
                    "placeholder": "Name",
                    "id": "floatingInput",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px;  font-weight:500; ",
                    "placeholder": "Email",
                    "id": "floatingInput",
                }
            ),
            "mobile": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px;font-weight:500; ",
                    "placeholder": "Mobile ..!",
                    "id": "floatingInput",
                }
            ),
            "current_company": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px;  font-weight:500; ",
                    "placeholder": "Current Company if any..!",
                    "id": "floatingInput",
                }
            ),
            "current_salary": NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px;font-weight:500; ",
                    "placeholder": "Your Current Salary..!",
                    "id": "floatingInput",
                }
            ),
            "expected_salary": NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px;font-weight:500; ",
                    "placeholder": "Expected Salary..!",
                    "id": "floatingInput",
                }
            ),
            "exprience": NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; font-weight:500; ",
                    "placeholder": "Total Exprience ..!",
                    "id": "floatingInput",
                }
            ),
            "skills": Textarea(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; font-weight:500; ",
                    "placeholder": "Your Domain & Skills ..!",
                    "id": "floatingInput",
                }
            ),
            "project_done": Textarea(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; font-weight:500; ",
                    "placeholder": "Name of Projects Done if any ..!",
                    "id": "floatingInput",
                }
            ),
            "awards": Textarea(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; font-weight:500; ",
                    "placeholder": "Awards & Achievments ..!",
                    "id": "floatingInput",
                }
            ),
            "address": Textarea(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; font-weight:500; ",
                    "placeholder": "Address ..!",
                    "id": "floatingInput",
                }
            ),
            "OnlineApplication": FileInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; font-weight:500; ",
                    "placeholder": "Message ..!",
                    "id": "floatingInput",
                }
            ),
        }

    def clean(self):
        # data from the form is fetched using super function
        super(OnlineApplicationForm, self).clean()
        # extract the username and text field from the data
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        mobile = self.cleaned_data.get("mobile")
        current_company = self.cleaned_data.get("current_company")
        current_salary = self.cleaned_data.get("current_salary")
        expected_salary = self.cleaned_data.get("expected_salary")
        exprience = self.cleaned_data.get("exprience")
        skills = self.cleaned_data.get("skills")
        project_done = self.cleaned_data.get("project_done")
        awards = self.cleaned_data.get("awards")
        address = self.cleaned_data.get("address")
        file = self.cleaned_data.get("file")

        # conditions to be met for the name length
        if len(name) < 5:
            self._errors["name"] = self.error_class(["Minimum 5 characters required"])
        if len(mobile) > 10:
            self._errors["mobile"] = self.error_class(["Only 10 Digit required"])

        if len(skills) < 10:
            self._errors["skills"] = self.error_class(
                ["Please Discribe Your Skill in more than 10 words"]
            )


class FeedBackForm(ModelForm):
    """Feedback form"""

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = FeedBack
        fields = ["email", "rating"]
        widgets = {
            "email": TextInput(
                attrs={
                    "class": "form-control ",
                    "style": "",
                    "placeholder": "Email",
                    "id": "floatingInput",
                }
            ),
            "rating": TextInput(
                attrs={
                    "class": "rate",
                    "style": "",
                    "placeholder": "rating",
                    "id": "floatingInput",
                    "type": "radio",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not re.match(REGEX, email):
            raise forms.ValidationError("Invalid email format")
        return email


class ContactForm(ModelForm):
    """contact form"""

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:50px; color:blue; font-weight:500; ",
                    "placeholder": "Name",
                    "id": "floatingInput",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:50px; color:blue; font-weight:500; ",
                    "placeholder": "Email",
                    "id": "floatingInput",
                    "type": "email",
                }
            ),
            "message": Textarea(
                attrs={
                    "class": "form-control ",
                    "style": "padding-left:50px; color:blue; font-weight:500; height:120px;",
                    "placeholder": "message",
                    "id": "floatingInput",
                }
            ),
        }
        # this function will be used for the validation

    def clean(self):
        # data from the form is fetched using super function
        super(ContactForm, self).clean()
        # extract the username and text field from the data
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        message = self.cleaned_data.get("message")

        # conditions to be met for the name length
        if len(name) < 5:
            self._errors["name"] = self.error_class(["Minimum 5 characters required"])
        if len(message) < 10:
            self._errors["message"] = self.error_class(
                ["Message Should Contain a minimum of 10 characters"]
            )
            # return any errors if found
        return self.cleaned_data


class OtpVerifyForm(forms.Form):
    """otp submit form"""

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    otp1 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )
    otp2 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )
    otp3 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )
    otp4 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )

    def clean(self):
        # data from the form is fetched using super function
        super(OtpVerifyForm, self).clean()
        otp1 = self.cleaned_data.get("otp1")
        otp2 = self.cleaned_data.get("otp2")
        otp3 = self.cleaned_data.get("otp3")
        otp4 = self.cleaned_data.get("otp4")

        # conditions to be met for the length
        if len(otp1) > 1:
            self._errors["otp1"] = self.error_class(["Only Single Digit"])
        if len(otp2) > 1:
            self._errors["otp2"] = self.error_class(["Only Single Digit"])
        if len(otp3) > 1:
            self._errors["otp3"] = self.error_class(["Only Single Digit"])
        if len(otp4) > 1:
            self._errors["otp4"] = self.error_class(["Only Single Digit"])


class DateForm(forms.Form):
    """date filter"""

    startdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                
                "class": "form-control",
                "type": "date",
                "style": "width: 200px;",
            }
        )
    )
    enddate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                
                "class": "form-control",
                "type": "date",
                "style": "width: 200px;",
            }
        )
    )
