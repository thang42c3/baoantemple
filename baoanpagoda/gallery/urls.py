from django.urls import path
from . import views

urlpatterns = [
    path('list_category', views.list_categories, name='list_category'),
]

