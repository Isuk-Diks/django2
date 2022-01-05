from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'news'
urlpatterns = [
    path('', cache_page(60*15)(views.IndexView.as_view()), name='index'),
    path('blog/', cache_page(60*15)(views.BlogListView.as_view()), name="blog"),
    path('detail-post/<slug:slug>/',views.ArticleDetailView.as_view(), name="detail_post"),
]
