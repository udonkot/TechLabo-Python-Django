from django.shortcuts import render

def azure(request):
  context = {
      'message': "Hello azure's Page!"
  }
  return render(request, 'apps/rooms/azure/main.html', context)
