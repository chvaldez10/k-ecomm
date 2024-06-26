from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Air bnb Backend APIs",
        default_version="v1",
        description="This is the documentation for the backend APIs",
        contact=openapi.Contact(email="christianvaldez021@gmail.com"),
        license=openapi.License(name="Chris License")
    ),
    public=True,
    permission_classes = (permissions.AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
