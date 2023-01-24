from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Add your urls here.
urlpatterns = [
    # 勉強会で使用するurls
    path('home', views.home, name='home'),
    path('sample', views.sample, name='sample'),
    path('okayasu', views.okayasu, name='okayasu'),
    path('hazeyama', views.hazeyama, name='hazeyama'),

    # slack APIお試し
    path('reactions', views.reactions, name='reactions'),

    # 勉強会で使用しないurls
    path('facescore', views.facescore, name='facescore'),    
    path('index', views.index, name='index')
]

if settings.DEBUG: 
  urlpatterns += static(
      settings.MEDIA_URL, 
      document_root = settings.MEDIA_ROOT
  )
