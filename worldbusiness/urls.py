from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from .docs import schema_view

admin.site.site_title = "WorldBusiness magazine administration"
admin.site.site_header = "WorldBusiness magazine Admin"
admin.site.index_title = "Site administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    # documentaion route...
    path("", schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)/$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("docs/swagger/", schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path("docs/redoc/", schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    # authentication routing
    path("accounts/", include('djoser.urls')),
    path("accounts/", include('djoser.urls.authtoken')),
    path("accounts/", include('djoser.urls.jwt')),
    # main
    path("", include('articles.urls')),

] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
