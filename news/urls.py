from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog/', views.BlogListView.as_view(), name="blog"),
    path('detail-post/<slug:slug>/', views.ArticleDetailView.as_view(), name="detail_post"),
]
