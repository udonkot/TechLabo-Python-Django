from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views as view_azure

# Add your urls here.
urlpatterns = [
  path('index', view_azure.azure, name='azureRoot'),
  path('facescore/', include('apps.azure.facescore.urls'), name='facescoreDir'),
]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
