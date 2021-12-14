from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_handler, name="blog"),
    path('detail-post/<slug:slug>/', views.detail_post, name="detail_post")
]
