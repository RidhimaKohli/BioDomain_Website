from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('instrumentlistpage', views.InstrumentListpage,name='instrumentlistpage'),
    path('institutelistpage', views.InstituteListpage,name='institutelistpage'),
    path('categorylistpage', views.CategoryListpage,name='categorylistpage'),
    path('team', views.team,name='team'),
]
