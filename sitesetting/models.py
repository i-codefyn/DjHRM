from django.db import models
import uuid
from django.urls import reverse


class Brands(models.Model):
    id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=150)
    pic = models.FileField(upload_to="upload/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("brand", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Brand"


class KeywordDiscription(models.Model):
    id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, editable=False
    )
    discription = models.TextField(max_length=255)
    keyword = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword

    def get_absolute_url(self):
        return reverse("keywords", args=[str(self.id)])


# class SitesFiles(models.Model):
#     id = models.UUIDField(
#         primary_key=True, db_index=True, default=uuid.uuid4, editable=False
#     )
#     title = models.CharField(max_length=100, help_text="Enter an image title")
#     image = models.ImageField(upload_to="images/")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name_plural = "SitesFiles"


class Sites(models.Model):
    id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, editable=False
    )
    domain_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    app_email = models.EmailField(max_length=100)
    app_mobile = models.CharField(max_length=20)
    app_address = models.TextField(max_length=150)
    app_version = models.CharField(max_length=20)
    app_logo = models.FileField(upload_to="upload/")
    app_fevicon = models.FileField(upload_to="upload/")
    app_stamp = models.FileField(upload_to="upload/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain_name

    def get_absolute_url(self):  # new
        return reverse("sites", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Sites"


class Features(models.Model):
    id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, editable=False
    )

    main_title = models.CharField(max_length=255)
    f1_title = models.CharField(max_length=255)
    f1 = models.CharField(max_length=255)
    f2_title = models.CharField(max_length=255)
    f2 = models.CharField(max_length=255)
    f3_title = models.CharField(max_length=255)
    f3 = models.CharField(max_length=255)
    f4_title = models.CharField(max_length=255)
    f4 = models.CharField(max_length=255)
    f5_title = models.CharField(max_length=255)
    f5 = models.CharField(max_length=255)
    f6_title = models.CharField(max_length=255)
    f6 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.main_title

    def get_absolute_url(self):
        return reverse("features", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Features"
        # indexes = [models.Index(fields=["id"], name="id_index")]


class Faq(models.Model):
    """
    faqs
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    que = models.CharField(max_length=255)
    ans = models.TextField(max_length=555)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.que

    def get_absolute_url(self):
        return reverse("faq", args=[str(self.id)])


class AboutCompany(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    about_company = models.TextField(max_length=555, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.about_company

    def get_absolute_url(self):
        return reverse("aboutcompany", args=[str(self.id)])


class SliderData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading1_title = models.CharField(max_length=255)
    heading1 = models.CharField(max_length=255)
    bg1 = models.FileField(upload_to="upload/", null=True, blank=True)
    heading2_title = models.CharField(max_length=255)
    heading2 = models.CharField(max_length=255)
    bg2 = models.FileField(upload_to="upload/", null=True, blank=True)
    heading3_title = models.CharField(max_length=255)
    heading3 = models.CharField(max_length=255)
    bg3 = models.FileField(upload_to="upload/", null=True, blank=True)
    heading4_title = models.CharField(max_length=255)
    heading4 = models.CharField(max_length=255)
    bg4 = models.FileField(upload_to="upload/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading1_title

    def get_absolute_url(self):  # new
        return reverse("slider", args=[str(self.id)])


class OurClients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("oc", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Our Clients"


class GoogleFeeds(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    google_feed = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.google_feed

    def get_absolute_url(self):
        return reverse("gf", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Google Feeds"
