from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='home'),
    path('form/', views.formEntry, name='form'),
    path('record/', views.recordData, name='record'),
    path('save/', views.saveData, name='save'),
]
