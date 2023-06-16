from django.urls import path
from . import views
urlpatterns = [
    path('photos_list/', views.photos_list, name='photos_list'),
    path('index/<str:pk>', views.index, name='index'),
]