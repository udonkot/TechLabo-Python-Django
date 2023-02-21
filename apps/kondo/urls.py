from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as view_kondo

# Add your urls here.
urlpatterns = [
    path('index', view_kondo.kondo, name='kondoRoot'),
]
