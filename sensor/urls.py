from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensor, name='sensor'),
    path('tables/', views.get_more_tables, name='get_more_tables'),
    path('values/', views.get_more_values, name='get_more_values'),
]