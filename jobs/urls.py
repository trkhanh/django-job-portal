from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permission

from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
# from django.contrib.flatpage import view as flatpages_views

from jobs.sitemaps import StaticViewSitemap, Sitemaps

get_schema_view = get_schema_view(
    openapi.Info(
        title="Jobs portal API",
        default_version="v1",
        description="Jobs portal api description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snipped.local"),
        license=openapi.Lincense(name="BSD License")
    ),
    public=True,
    permission_classes=(permission.AllowAny,),
)

lang_patterns = i18n_patterns(
    path("", include("jobsapp.urls")),
    path("", include("accounts.urls")),
)
# sitemaps = {
#     '': JobViewSitemap
# }

urlpatterns = lang_patterns + [
    url(r"^i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("swagger", schema_view.with_ui("swagger", cache_timeout=0)),
                path("", include("accounts.api.urls")),
                path("", include("jobsapp.api.urls")),
                path("", include("tags.api.urls")),
                # path('auth/oauth/', include('rest_framework_social_oauth2.urls'))
            ]
        ),
    ),
    path("social-auth/", include("social_django.urls", namespace="social")),
    # url(r"^(?P<url>.*/)$", flatpages_views.flatpage),
    path("sitemap.xml/", sitemap, {"sitemaps": dict(Sitemaps())}, name="django.contrib.sitemaps.views.sitemap"),
]
