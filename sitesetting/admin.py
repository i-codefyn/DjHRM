from django.contrib import admin
from .models import (
    Sites,
    Features,
    Faq,
    OurClients,
    SliderData,
    AboutCompany,
    GoogleFeeds,
    KeywordDiscription,
    Brands,
    OurClients,
    GoogleFeeds,
)


class GoogleFeedsAdmin(admin.ModelAdmin):
    list_display = [
        "google_feed",
    ]


admin.site.register(GoogleFeeds, GoogleFeedsAdmin)


class OurClientsAdmin(admin.ModelAdmin):
    list_display = ["name", "review"]


admin.site.register(OurClients, OurClientsAdmin)


class BrandsAdmin(admin.ModelAdmin):
    list_display = ["name", "pic"]


admin.site.register(Brands, BrandsAdmin)


class KeywordDiscriptionAdmin(admin.ModelAdmin):
    list_display = ["keyword", "discription"]


admin.site.register(KeywordDiscription, KeywordDiscriptionAdmin)


class SitesAdmin(admin.ModelAdmin):
    list_display = (
        "domain_name",
        "display_name",
        "app_version",
        "app_logo",
        "app_fevicon",
        "app_email",
        "app_mobile",
        "app_address",
        "app_version",
        "app_stamp",
    )


admin.site.register(Sites, SitesAdmin)


class FeaturesAdmin(admin.ModelAdmin):
    list_display = (
        "main_title",
        "f1",
        "f1_title",
        "f2",
        "f2_title",
        "f3",
        "f3_title",
        "f4",
        "f4_title",
        "f5",
        "f5_title",
        "f6",
        "f6_title",
    )


admin.site.register(Features, FeaturesAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ("que", "ans")


admin.site.register(Faq, FaqAdmin)


class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ["about_company"]


admin.site.register(AboutCompany, AboutCompanyAdmin)


class SliderDataAdmin(admin.ModelAdmin):
    list_display = (
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
    )


admin.site.register(SliderData, SliderDataAdmin)
