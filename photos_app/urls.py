from django.urls import path
from . import views
urlpatterns = [
    path('', views.photos_list, name='photos_list'),
    path('index/<str:pk>', views.index, name='index'),
]