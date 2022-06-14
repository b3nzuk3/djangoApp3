from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_links),
    path('images/', views.get_images),
    path('image/<pk>', views.single_image),
    path('profiles/', views.get_profiles),
    path('profile/<pk>', views.single_profile),
]
