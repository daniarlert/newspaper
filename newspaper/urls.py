"""
URL configuration for newspaper project.
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
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
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
