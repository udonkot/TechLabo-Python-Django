from django.urls import path
from apps.azure import views as view_azure

# Add your urls here.
urlpatterns = [
  path('init', view_azure.facescoreinit, name='azureFaceScore'),
  path('', view_azure.facescore, name='azureFaceScore'),

]
