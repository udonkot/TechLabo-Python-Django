from django.urls import path
from apps.azure import views as view_azure
from . import views as view_facescore

# Add your urls here.
urlpatterns = [
  path('init', view_facescore.facescoreinit, name='azureFaceScore'),
  path('', view_facescore.facescore, name='azureFaceScore'),

]
