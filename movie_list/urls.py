from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('gallery/', views.gallery, name='gallery'),
    path('movie_info/<int:pk>', views.movie_info, name='movie_info'),
    path('show_info/<int:pk>', views.show_info, name='show_info'),
    path('remove_movie/<str:pk>', views.remove_movie, name='remove_movie'),
    path('remove_show/<str:pk>', views.remove_show, name='remove_show'),
]
