from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as view_slackapi

# Add your urls here.
urlpatterns = [
  path('', view_slackapi.slackapi, name='slackapi'),
  path('/reaction/init', view_slackapi.init, name='init'),
  path('/reaction/summary', view_slackapi.summary, name='summary'),
]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
