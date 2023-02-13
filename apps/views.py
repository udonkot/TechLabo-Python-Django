import base64
from email.mime import image
from pickle import FALSE
from django.shortcuts import render
from PIL import Image

from apps.models import Upload

from apps.main import getFaceSample, showFaceLog

from facescore.settings import MEDIA_ROOT

# Create your views here.
# 勉強会で使用するviews
def home(request):
  return render(request, 'apps/body.html')

def sample(request):
  context = {
      'message': "Hello sample's Page!"
  }
  return render(request, 'apps/rooms/sample/main.html', context)

def okayasu(request):
  context = {
      'message': "Hello okayasu's Page!"
  }
  return render(request, 'apps/rooms/okayasu/main.html', context)

def hazeyama(request):
  context = {
      'message': "Hello hazeyama's Page!"
  }
  return render(request, 'apps/rooms/hazeyama/main.html', context)

# 勉強会で使用しないviews
def index(request):
  context = {
      'title': 'test page'
  }
  return render(request, 'apps/index.html', context)
