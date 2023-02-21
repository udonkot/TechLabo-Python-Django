from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from . import views as view_slackapi

# Add your urls here.
urlpatterns = [
  path('index', view_slackapi.slackapi, name='slackapiRoot'),
  path('reaction/', include('apps.slackapi.reaction.urls'), name='reactionDir'),

]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
