from django.shortcuts import render

def kondo(request):
  context = {
      'message': "Hello kondo's Page!"
  }
  return render(request, 'apps/rooms/kondo/main.html', context)
