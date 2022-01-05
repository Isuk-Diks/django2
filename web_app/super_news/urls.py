from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
import debug_toolbar
from news.sitemap import ArticleSitemap


urlpatterns = [
    path("", include('news.urls')),
    path("accounts/", include("client_profile.urls")),
    path("search/", include("search.urls")),
    path('grappelli/', include('grappelli.urls')),
    path('accounts/', include('allauth.urls')),
    path('sitemap.xml/', sitemap, {"sitemaps":{
                                    'articles': ArticleSitemap}},
     name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
