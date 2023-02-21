from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views as view_reaction

# Add your urls here.
urlpatterns = [
  path('init', view_reaction.init, name='init'),
  path('summary', view_reaction.summary, name='summary'),
]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
