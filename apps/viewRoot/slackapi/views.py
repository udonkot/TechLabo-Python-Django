from django.shortcuts import render

def slackapi(request):
  context = {
      'message': "Hello slackapi's Page!"
  }
  return render(request, 'apps/rooms/slackapi/main.html', context)

def init(request):
  return render(request, 'apps/rooms/slackapi/reaction/summary.html')

def summary(request):

  dummyUserId = request.POST.get('userId','xyz');
  dummyMonth = request.POST.get('month',0)
  context = {
    'responseList': [
      {
        'rank': 1,
        'userId': 'user01',
        'emojiName': 'hoge',
        'emoji': '',
        'cnt': 500
      },
      {
        'rank': 2,
        'userId': 'user02',
        'emojiName': 'piyo',
        'emoji': '',
        'cnt': 200
      },
      {
        'rank': 3,
        'userId': 'user03',
        'emojiName': 'fuga',
        'emoji': '',
        'cnt': 50
      },
      {
        'rank': 99,
        'userId': dummyUserId,
        'emojiName': 'zzzz',
        'emoji': '',
        'cnt': dummyMonth
      },
    ]
  }

  return render(request, 'apps/rooms/slackapi/reaction/summary.html', context)

