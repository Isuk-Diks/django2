from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_handler, name="blog_handler"),
    path('detail-post/', views.blog_handler, name="detail_post")
]