from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='image-home'),
    path('search_results/', views.search, name='image-search'),
]
