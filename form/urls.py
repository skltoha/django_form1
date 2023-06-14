from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('form/', views.formEntry, name='form'),
    path('record/', views.recordData, name='record'),
    path('save/', views.saveData, name='save'),
    path('userinfo/<int:stdid>', views.userinfo, name='userinfo'),
    path('userinfoedit/<int:stdid>/', views.userinfoedit, name='userinfoedit'),
    path('update/<int:stdid>/', views.update, name='update'),
    path('delete/<int:stdid>/', views.delete, name='delete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
