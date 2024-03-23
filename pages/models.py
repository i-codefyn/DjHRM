from django.db import models
import uuid
from django.urls import reverse

from django.core.exceptions import ValidationError


def validate_email(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("Accepted ! Mail id of google only")


def photo_size(value):  # add this to some file where you can import it from
    limit = 50 * 1024
    limit_Low = 20 * 1024
    if value.size > limit:
        raise ValidationError("File too large. Size should not exceed 50 kb.")
    if value.size < limit_Low:
        raise ValidationError("File too Small. Size should not less than 20 kb.")


def sign_size(value):  # add this to some file where you can import it from
    limit = 20 * 1024
    limit_Low = 10 * 1024
    if value.size > limit:
        raise ValidationError("File too large. Size should not exceed 20 kb.")
    if value.size < limit_Low:
        raise ValidationError("File too Small. Size should not less than 10 kb.")


def resume_size(value):  # add this to some file where you can import it from
    limit = 50 * 1024 * 1024
    if value.size > limit:
        raise ValidationError("File too large. Size should not exceed 2 Mb.")


def application_id():
    number = "CFYN" + (str(uuid.uuid4()).split("-")[1]).upper()
    return number


class OnlineApplication(models.Model):
    """Create Model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application_no = models.CharField(
        max_length=255, default=application_id, unique=True, editable=False
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, validators=[validate_email])
    mobile = models.CharField(max_length=10)
    current_company = models.CharField(max_length=255)
    current_salary = models.CharField(max_length=255)
    expected_salary = models.IntegerField()
    exprience = models.IntegerField()
    skills = models.TextField(max_length=555)
    project_done = models.TextField(max_length=555, null=True, blank=True)
    address = models.TextField(max_length=555, null=True, blank=True)
    awards = models.TextField(max_length=555, null=True, blank=True)
    resume = models.FileField(upload_to="upload", validators=[resume_size])
    photo = models.ImageField(upload_to="upload", validators=[photo_size])
    sign = models.ImageField(upload_to="upload", validators=[sign_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("online_application", args=[str(self.id)])


class JobPortal(models.Model):
    """Job"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=555)
    exprience = models.IntegerField()
    salary = models.CharField(max_length=254)
    apply_link = models.CharField(max_length=255)
    last_date = models.DateField()

    def __str__(self):
        return self.post_name

    def get_absolute_url(self):
        return reverse("job", args=[str(self.id)])


class FeedBack(models.Model):
    """Feedback"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=50, validators=[validate_email])
    rating = models.CharField(max_length=5)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("feedback", args=[str(self.id)])


class ContactUs(models.Model):
    """Contact form"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, validators=[validate_email])
    message = models.TextField(max_length=254)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("msg", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Contact Us"


# class OnlineRequest(models.Model):
#     """Online Request Create Model"""

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254, validators=[validate_email])
#     message = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("online_requests", args=[str(self.id)])
