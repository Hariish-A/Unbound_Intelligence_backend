from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Chat App API",
        default_version='v1',
        description="This is the API documentation for the Unbound Hackathon Chat App. It allows you to generate chat "
                    "completions,"
                    "interact with different models, and perform other chat-related operations.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@chatapp.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,]
)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('v1/', include('apis.urls')),
]