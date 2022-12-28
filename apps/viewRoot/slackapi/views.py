from django.shortcuts import render

def slackapi(request):
  context = {
      'message': "Hello slackapi's Page!"
  }
  return render(request, 'apps/rooms/slackapi/main.html', context)

def init(request):
  return render(request, 'apps/rooms/slackapi/reaction/summary.html')