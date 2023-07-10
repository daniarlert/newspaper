"""
URL configuration for newspaper project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("articles/", include("articles.urls")),
    path("", include("pages.urls")),
    # Third party
    path("__debug__/", include("debug_toolbar.urls")),
]
