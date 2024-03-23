from django.contrib import admin
from .models import ContactUs, FeedBack, OnlineApplication, JobPortal


class OnlineApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "mobile",
    ]


admin.site.register(OnlineApplication, OnlineApplicationAdmin)


class JobPortalAdmin(admin.ModelAdmin):
    list_display = [
        "post_name",
        "descriptions",
        "exprience",
        "salary",
        "apply_link",
    ]


admin.site.register(JobPortal, JobPortalAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "message",
    ]


admin.site.register(ContactUs, ContactUsAdmin)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "rating",
    ]


admin.site.register(FeedBack, FeedBackAdmin)
