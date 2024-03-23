from django.urls import path

from users.views import SignupPageView, StaffView, UserAcountView
from users.staff.services import StaffViewServices
from users.staff.sliders import (
    SliderList,
    SliderCreate,
    SliderDetail,
    SliderDelete,
    SliderExportPdfAll,
    SliderUpdate,
    SliderExportPdfbyDate,
    SliderExportPdfbyId,
    SliderExportCsv,
)
from users.staff.users import (
    UsersDetail,
    UsersExportPdfAll,
    UsersExportPdfbyId,
    UsersExportCsv,
    UsersList,
    UsersExportPdfbyDate,
)
from users.staff.sites import (
    SitesList,
    SitesDetail,
    SitesCreate,
    SitesUpdate,
    SitesDelete,
)
from users.staff.kewords import (
    KeywordsDiscriptionsList,
    KeywordsDiscriptionsDetail,
    KeywordDiscriptionCreate,
    KeywordDiscriptionDelete,
    KeywordDiscriptionUpdate,
)

from users.staff.features import (
    FeaturesList,
    FeaturesDetail,
    FeaturesDelete,
    FeaturesCreate,
    FeaturesUpdate,
)
from users.staff.aboutcompany import (
    AboutCompanyList,
    AboutCompanyCreate,
    AboutCompanyDelete,
    AboutCompanyDetail,
    AboutCompanyUpdate,
)
from users.staff.faq import FaqCreate, FaqDetail, FaqList, FaqUpdate, FaqDelete
from users.staff.oc import (
    ClientCreate,
    ClientDetail,
    ClientList,
    ClientUpdate,
    ClientDelete,
)
from users.staff.gf import GfCreate, GfDetail, GfUpdate, GfList, GfDelete
from users.staff.brand import (
    BrandList,
    BrandDetail,
    BrandDelete,
    BrandCreate,
    BrandUpdate,
    BrandExportPdfAll,
    BrandExportCsv,
)
from users.staff.JobsPortal import (
    JobsList,
    JobCreate,
    JobDetail,
    JobUpdate,
    JobDelete,
)
from users.staff.OnlineApplication import (
    OnlineApplicationList,
    OnlineApplicationDetails,
    OnlineApplicationExportPdfAll,
    OnlineRequetsExportPdfbyId,
)

from users.staff.feedback import FeedbackList
from users.staff.messages import MessageList

urlpatterns = [
    path("staff/", StaffView.as_view(), name="staff"),
    # Alerts
    path("staff/feedback", FeedbackList.as_view(), name="feedback_list"),
    path("staff/msg", MessageList.as_view(), name="msg_list"),
    path(
        "staff/JobPortal/<uuid:pk>/delete",
        JobDelete.as_view(),
        name="job_delete",
    ),
    path(
        "staff/JobPortal/<uuid:pk>/update",
        JobUpdate.as_view(),
        name="job_update",
    ),
    path(
        "staff/JobPortal/<uuid:pk>",
        JobDetail.as_view(),
        name="job",
    ),
    path(
        "staff/JobPortal",
        JobsList.as_view(),
        name="job_list",
    ),
    path(
        "staff/JobCreate",
        JobCreate.as_view(),
        name="job_create",
    ),
    path(
        "staff/OnlineApplication",
        OnlineApplicationList.as_view(),
        name="online_application_list",
    ),
    path(
        "staff/OnlineApplication/<uuid:pk>",
        OnlineApplicationDetails.as_view(),
        name="online_application",
    ),
    path(
        "staff/OnlineApplication/ExportPdfAll",
        OnlineApplicationExportPdfAll,
        name="online_application_pdf_all",
    ),
    # path(
    #     "staff/OnlineApplication/ExportPdfFiltered",
    #     OnlineRequetsExportPdfbyDate,
    #     name="online_requests_list_pdf_export_bydate",
    # ),
    path(
        "staff/OnlineApplication/<uuid:pk>/pdf",
        OnlineRequetsExportPdfbyId,
        name="online_requests_list_pdf_export_by_id",
    ),
    # path(
    #     "staff/OnlineApplication/Csv",
    #     OnlineApplicationExportCsv,
    #     name="online_requests_list_export_csv",
    # ),
    # staff brand
    path("staff/brand", BrandList.as_view(), name="brand_list"),
    path("staff/brand/<uuid:pk>", BrandDetail.as_view(), name="brand"),
    path("staff/brand/<uuid:pk>/update", BrandUpdate.as_view(), name="brand_update"),
    path("staff/brand/<uuid:pk>/delete", BrandDelete.as_view(), name="brand_delete"),
    path("staff/brand/create", BrandCreate.as_view(), name="brand_create"),
    path("staff/brand/PDFall", BrandExportPdfAll, name="brand_export_pdf_all"),
    path("staff/brand/CSV", BrandExportCsv, name="brand_export_csv"),
    # staff GoogleFeeds
    path("staff/gf", GfList.as_view(), name="gf_list"),
    path("staff/gf/<uuid:pk>", GfDetail.as_view(), name="gf"),
    path("staff/gf/<uuid:pk>/update", GfUpdate.as_view(), name="gf_update"),
    path("staff/gf/<uuid:pk>/delete", GfDelete.as_view(), name="gf_delete"),
    path("staff/gf/create", GfCreate.as_view(), name="gf_create"),
    # staff OurClients
    path("staff/oc", ClientList.as_view(), name="oc_list"),
    path("staff/oc/create", ClientCreate.as_view(), name="oc_create"),
    path("staff/oc/<uuid:pk>", ClientDetail.as_view(), name="oc"),
    path("staff/oc/<uuid:pk>/update", ClientUpdate.as_view(), name="oc_update"),
    path("staff/oc/<uuid:pk>/delete", ClientDelete.as_view(), name="oc_delete"),
    # staff Faq
    path("staff/faq", FaqList.as_view(), name="faq_list"),
    path("staff/faq/create", FaqCreate.as_view(), name="faq_create"),
    path("staff/faq/<uuid:pk>", FaqDetail.as_view(), name="faq"),
    path("staff/faq/<uuid:pk>/update", FaqUpdate.as_view(), name="faq_update"),
    path("staff/faq/<uuid:pk>/delete", FaqDelete.as_view(), name="faq_delete"),
    # staff AboutCompany
    path("staff/aboutcompany", AboutCompanyList.as_view(), name="aboutcompany_list"),
    path(
        "staff/aboutcompany/create",
        AboutCompanyCreate.as_view(),
        name="aboutcompany_create",
    ),
    path(
        "staff/aboutcompany/<uuid:pk>",
        AboutCompanyDetail.as_view(),
        name="aboutcompany",
    ),
    path(
        "staff/aboutcompany/<uuid:pk>/delete",
        AboutCompanyDelete.as_view(),
        name="aboutcompany_delete",
    ),
    path(
        "staff/aboutcompany/<uuid:pk>/update",
        AboutCompanyUpdate.as_view(),
        name="aboutcompany_update",
    ),
    # staff Features
    path("staff/features", FeaturesList.as_view(), name="feature_list"),
    path("staff/features/create", FeaturesCreate.as_view(), name="feature_create"),
    path(
        "staff/features/<uuid:pk>/delete",
        FeaturesDelete.as_view(),
        name="feature_delete",
    ),
    path("staff/features/<uuid:pk>", FeaturesDetail.as_view(), name="features"),
    path(
        "staff/features/<uuid:pk>/update",
        FeaturesUpdate.as_view(),
        name="features_update",
    ),
    # staff kewords
    path("staff/keywords", KeywordsDiscriptionsList.as_view(), name="keywords_list"),
    path(
        "staff/keywords/create",
        KeywordDiscriptionCreate.as_view(),
        name="keywords_create",
    ),
    path(
        "staff/keywords/<uuid:pk>",
        KeywordsDiscriptionsDetail.as_view(),
        name="keywords",
    ),
    path(
        "staff/keywords/<uuid:pk>/delete",
        KeywordDiscriptionDelete.as_view(),
        name="keywords_delete",
    ),
    path(
        "staff/keywords/<uuid:pk>/update",
        KeywordDiscriptionUpdate.as_view(),
        name="keywords_update",
    ),
    # staff site setting  section
    path("staff/sites", SitesList.as_view(), name="site_list"),
    path("staff/sites/<uuid:pk>", SitesDetail.as_view(), name="sites"),
    path("staff/sites/<uuid:pk>/update", SitesUpdate.as_view()),
    path("staff/sites/<uuid:pk>/delete", SitesDelete.as_view()),
    path("staff/sites/Create", SitesCreate.as_view(), name="sites_create"),
    # staff users section
    path("staff/users", UsersList.as_view(), name="users_list"),
    path(
        "staff/users/exportpdfbydate", UsersExportPdfbyDate, name="users_export_bydate"
    ),
    path("staff/users/pdf", UsersExportPdfAll, name="users_exportpdf_all"),
    path("staff/users/csv", UsersExportCsv, name="users_exportcsv"),
    path("staff/users/<uuid:pk>/pdf", UsersExportPdfbyId, name="users_exportpdf_byid"),
    path("staff/users/<uuid:pk>", UsersDetail.as_view(), name="users"),
    path("staff/services", StaffViewServices.as_view(), name="staff-view-services"),
    path("accounts/profile/", UserAcountView.as_view(), name="user-profile"),
    # staff sliders
    path("staff/slider", SliderList.as_view(), name="slider_list"),
    path("staff/slider/create", SliderCreate.as_view(), name="slider_create"),
    path("staff/slider/<uuid:pk>", SliderDetail.as_view(), name="slider"),
    path("staff/slider/<uuid:pk>/update", SliderUpdate.as_view(), name="slider_update"),
    path("staff/slider/<uuid:pk>/delete", SliderDelete.as_view(), name="slider_delete"),
    path("staff/slider/exportpdfall", SliderExportPdfAll, name="slider_exportpdf_all"),
    path("staff/slider/<uuid:pk>/pdf", SliderExportPdfbyId),
    path("staff/s", SliderExportCsv, name="slider_exportcsv"),
    path(
        "staff/slider/exportpdfbydate",
        SliderExportPdfbyDate,
        name="slider_exportpdf_bydate",
    ),
]
