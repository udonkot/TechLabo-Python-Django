from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as view_azure

# Add your urls here.
urlpatterns = [
  path('', view_azure.azure, name='azureHome'),
  path('facescore/init', view_azure.facescoreinit, name='azureFaceScore'),
  path('facescore', view_azure.facescore, name='azureFaceScore'),
]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
