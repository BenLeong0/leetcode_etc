from django.urls import path

from . import views

urlpatterns = [
               path('', views.index, name='index'),
               path('get_token/', views.auth_and_get_token, name='get_token'),
               path('create_user/', views.create_user, name='create_user'),
               path('get_user/', views.get_user, name='get_user'),
               path('generate_reset_token/', views.generate_reset_token, name='generate_reset_token'),
               path('reset_password/', views.reset_password, name='reset_password'),
              ]

