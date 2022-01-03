from django.urls import path

from . import views

app_name = 'profile'
urlpatterns = [
    path('profile/', views.my_profile, name="my_profile"),
    path('profile/<str:username>', views.profile, name="profile"),
]
