from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Add your urls here.
urlpatterns = [
    # 勉強会で使用するurls
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sample', views.sample, name='sample'),
    path('okayasu', views.okayasu, name='okayasu'),
    path('hazeyama', views.hazeyama, name='hazeyama'),
    path('kondo', include('apps.kondo.urls'), name='kondoDir'),
    path('slackapi', include('apps.slackapi.urls'), name='slackapiDir'),
    path('azure', include('apps.azure.urls'), name='azureDir'),

    # 勉強会で使用しないurls
    path('index', views.index, name='index')
]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
