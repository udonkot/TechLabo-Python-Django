from django.shortcuts import render

# Create your views here.
def index(request):
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
