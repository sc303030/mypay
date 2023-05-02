from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
]


if settings.DEBUG:
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
