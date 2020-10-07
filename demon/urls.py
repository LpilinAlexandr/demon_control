from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='news'),
    path('ajax_form/', views.ajax_form, name='ajax_form')
]