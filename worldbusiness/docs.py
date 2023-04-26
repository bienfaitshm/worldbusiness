
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

DESCRIPTION = """
    documentation of world business
    
"""

schema_view = get_schema_view(
    openapi.Info(
        title="worldbusiness Api DOCUMENTATION",
        default_version='v1',
        description=DESCRIPTION,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bienfaitshm@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
