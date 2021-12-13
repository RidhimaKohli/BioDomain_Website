from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('instrumentlistpage', views.InstrumentListpage,name='instrumentlistpage'),
    path('institutelistpage', views.InstituteListpage,name='institutelistpage'),
    path('categorylistpage', views.CategoryListpage,name='categorylistpage'),
    path('team', views.team,name='team'),
    path('trial', views.trial,name='trial'),
    path('BasicEquipments', views.BasicEquipments,name='BasicEquipments'),
    path('BioimagingEquipments', views.BioimagingEquipments,name='BioimagingEquipments'),
    path('CentrifugeEquipments', views.CentrifugeEquipments,name='CentrifugeEquipments'),
    path('CellCultureEquipments', views.CellCultureEquipments,name='CellCultureEquipments'),
    path('ElectrophoresisEquipments', views.ElectrophoresisEquipments,name='ElectrophoresisEquipments'),
    path('ChromatographyEquipments', views.ChromatographyEquipments,name='ChromatographyEquipments'),
    path('SpectroscopyEquipments', views.SpectroscopyEquipments,name='SpectroscopyEquipments'),
    path('XrayCrystallographyEquipments', views.XrayCrystallographyEquipments,name='X-rayCrystallographyEquipments'),
    path('SequencingEquipments', views.SequencingEquipments,name='SequencingEquipments'),
    path('PCREquipments', views.PCREquipments,name='PCREquipments'),
    path('RefrigeratorEquipments', views.RefrigeratorEquipments,name='RefrigeratorEquipments'),
    path('IncubatorEquipments', views.IncubatorEquipments,name='IncubatorEquipments'),
    path('BioreactorEquipments', views.BioreactorEquipments,name='BioreactorEquipments'),
    path('MiscellaneousEquipments', views.MiscellaneousEquipments,name='MiscellaneousEquipments'),
    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
]
