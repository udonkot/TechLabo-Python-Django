from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Add your urls here.
urlpatterns = [
    # アプリ用のurls
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sample', views.sample, name='sample'),
    path('slackapi/', include('apps.slackapi.urls'), name='slackapiDir'),
    path('azure/', include('apps.azure.urls'), name='azureDir'),
    path('index', views.index, name='index'),

    # ユーザ用のURL
    # apps/{ユーザ名}配下のurls.pyへリクエストを転送する
    #path('irito/', include('apps.irito.urls')),
    path('okayasu/', include('apps.okayasu.urls')),
    #path('kondo/', include('apps.kondo.urls')),
    #path('kita/', include('apps.kita.urls')),
    #path('hazama/', include('apps.hazama.urls')),
    #path('hazeyama/', include('apps.hazeyama.urls')),
    #path('matsuura/', include('apps.matsuura.urls')),
    #path('yamane/', include('apps.yamane.urls')),

    #path('hazeyama/', views.hazeyama, name='hazeyama'),
    path('kondo/', include('apps.kondo.urls'), name='kondoDir'),
]

if settings.DEBUG:
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT
  )
