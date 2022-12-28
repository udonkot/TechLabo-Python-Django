from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from apps.viewRoot.kondo import views as view_kondo
from apps.viewRoot.slackapi import views as view_slackapi

# Add your urls here.
urlpatterns = [
    # 勉強会で使用するurls
    path('home', views.home, name='home'),
    path('sample', views.sample, name='sample'),
    path('okayasu', views.okayasu, name='okayasu'),
    path('hazeyama', views.hazeyama, name='hazeyama'),
    path('kondo', view_kondo.kondo, name='kondo'),
    path('slackapi', view_slackapi.slackapi, name='slackapi'),
    path('slackapi/reaction/init', view_slackapi.init, name='summary'),

    # 勉強会で使用しないurls
    path('facescore', views.facescore, name='facescore'),
    path('index', views.index, name='index')
]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
