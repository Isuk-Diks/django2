from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
urlpatterns = [
    path("", include('news.urls')),
    path("accounts/", include("client_profile.urls")),
    path("search/", include("search.urls")),
    path('grappelli/', include('grappelli.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
