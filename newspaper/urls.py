"""
URL configuration for newspaper project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("django.contrib.auth.urls")),
    # Local apps
    path("accounts/", include("accounts.urls")),
    path("articles/", include("articles.urls")),
    path("", include("pages.urls")),
]
