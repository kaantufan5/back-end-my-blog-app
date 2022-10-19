from django.contrib import admin
from django.urls import path, include

# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Blog App API",
        default_version="v1",
        description="The input, output, and remaining amount of stock products",
        terms_of_service="#",
        contact=openapi.Contact(email="abdullahkaantufan6@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Url paths for swagger:
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path('users/', include('users.urls')),
    path('blogs/', include('blogs.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
