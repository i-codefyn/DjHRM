from django.urls import path, include

from .views import (
    ServicesListViews,
    ServicesDetailViews,
    PersonalSites,
    Ecommerce,
    MobileApp,
    Cms,
    Hrm,
    Portfollio,
    StaticSites,
    Blogs,
)


urlpatterns = [
    path(
        "services/PersonalSites",
        PersonalSites.as_view(),
        name="personal_sites",
    ),
    path(
        "services/OnlineStores",
        Ecommerce.as_view(),
        name="online_stores",
    ),
    path("services/MobileWebApp", MobileApp.as_view(), name="mobile_web_app"),
    path("services/CMS", Cms.as_view(), name="cms"),
    path("services/HRM", Hrm.as_view(), name="hrm"),
    path("services/Portfollio", Portfollio.as_view(), name="portfollio"),
    path("services/Blogs", Blogs.as_view(), name="blogs"),
    path("services/StaticSites", StaticSites.as_view(), name="static_sites"),
    path("services/", ServicesListViews.as_view(), name="services"),
    path("services/<uuid:pk>", ServicesDetailViews.as_view(), name="service_detail"),
]
