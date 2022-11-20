from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Add your urls here.
urlpatterns = [
    path('facescore', views.facescore, name='facescore'),    
    path('index', views.index, name='index'),
    path('sample', views.sample, name='sample'),
    path('okayasu', views.okayasu, name='okayasu'),
]

if settings.DEBUG: 
  urlpatterns += static(
      settings.MEDIA_URL, 
      document_root = settings.MEDIA_ROOT
  )
