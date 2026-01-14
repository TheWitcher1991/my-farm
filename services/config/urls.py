from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from config.os import DEBUG
from config.settings import ADMIN_URL
from packages.kernel.utils import t

app_name = "config"

admin.site.index_title = t("Моя ферма")

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path(f"{ADMIN_URL}doc/", include("django.contrib.admindocs.urls")),
    path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-docs",
    ),
    path("v1/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("", include("django_prometheus.urls")),
    path("v1/", include("articles.routers", namespace="articles")),
    path("v1/", include("auth.routers", namespace="auth")),
    path("v1/", include("calculators.routers", namespace="calculators")),
    path("v1/", include("categories.routers", namespace="categories")),
    path("v1/", include("diseases.routers", namespace="diseases")),
    path("v1/", include("documents.routers", namespace="documents")),
    path("v1/", include("feeds.routers", namespace="feeds")),
    path("v1/", include("users.routers", namespace="users")),
]

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
