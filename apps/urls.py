from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('facescore', views.facescore, name='facescore'),    
]

if settings.DEBUG: 
  urlpatterns += static(
      settings.MEDIA_URL, 
      document_root = settings.MEDIA_ROOT
  )
