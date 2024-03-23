from django.urls import path

from pages.views import (
    JobApply,
    HomePage,
    AboutUs,
    FaqsView,
    TermsAndConditionsView,
    DisclamerView,
    OtpVerify,
    FeedBackFormView,
    SendHTMLMail,
    OtpReset,
    ContactFormView,
    OurWorks,
    JobPortal,
    UploadFile,
)


urlpatterns = [
    path("", HomePage.as_view(), name="Home"),
    path("jobs/apply", JobApply.as_view(), name="apply_link"),
    path("jobs/", JobPortal.as_view(), name="jobs_portal"),
    path("jobs/FinalSubmit", UploadFile.as_view(), name="upload_file"),
    # path("", HomePageView.as_view()),
    path("works/", OurWorks.as_view(), name="works"),
    path("OtpVerify/", OtpVerify.as_view(), name="otp_verify"),
    path("OtpResend/", OtpReset, name="otp_reset"),
    path("aboutus/", AboutUs.as_view(), name="aboutus"),
    path("contactus/", ContactFormView.as_view(), name="contactus"),
    path("feedback/", FeedBackFormView.as_view(), name="feedback"),
    path("faqs/", FaqsView.as_view(), name="faqs"),
    path("disclamer/", DisclamerView.as_view(), name="disclamer"),
    path(
        "terms-conditions/",
        TermsAndConditionsView.as_view(),
        name="terms_and_conditions",
    ),  # new
]
