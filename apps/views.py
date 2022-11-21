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

def facescore(request):
  
  if request.method == 'POST':
    
    fileTitle = request.POST.get("fileTitle",FALSE)
    uploadFile = request.FILES.get("uploadFile", FALSE)
    
    up = Upload(
      title = fileTitle,
      uploadFile = uploadFile,
      uploadBinary = uploadFile,
      uploadImage = uploadFile,
    )
  
    documents = Upload.objects.all()

  
#    encodeData = ""
#    print("base64:")
#    encodeData = base64.b64encode(Upload.uploadeBinary.read()).decode("ascii")
#    encodeData = base64.b64encode(uploadFile.read()).decode("ascii")

    imageData = Image.open(uploadFile)
    print('size')
    print('width:' + str(imageData.width)) 
    print('height:' + str(imageData.height)) 
    

    fname = MEDIA_ROOT + '/uploads/' + 'aaa.jpg'
    f = open(fname, 'wb+')
    for chunk in uploadFile.chunks():
      f.write(chunk)
    f.close
    
    ret = getFaceSample(fname)
    
    sumary = calcSummaryFaceScore(ret);
    
    if not ret :
      context = {
        'files': documents,
        'title': fileTitle,
        'error': '画像から人物を特定できませんでした。。。'
      }
    else :
      context = {
        'files': documents,
        'title': fileTitle,
#     'uploadfile': base64.b64encode(Upload.uploaderFile),
#      'uploadfile': encodeData,
       'detected_faces': ret,
       'summary': sumary,
#      'img': drawFaceRectangles(),
      }

    
  else:
    context = {
      'title': "",
#      'img': drawFaceRectangles(),
    }
       
  # Uncomment this to show the face rectangles.

  return render(request, 'apps/facescore.html', context)

def calcSummaryFaceScore(detected_faces) :
  smile = 0;
  happiness = 0;
  anger = 0;
  sadness = 0;
  surprise = 0;
  fear = 0;
  contempt = 0;
  disgust = 0;
  neutral = 0;
  
  for faceData in detected_faces :
    # 笑顔度
    smile += faceData[0].face_attributes.smile;
    # 幸福度
    happiness += faceData[0].face_attributes.emotion.happiness;
    # 怒り度</th>
    anger += faceData[0].face_attributes.emotion.anger;
    # 悲しみ度</th>
    sadness += faceData[0].face_attributes.emotion.sadness;
    # 驚き度</th>
    surprise += faceData[0].face_attributes.emotion.surprise;
    # 恐怖度</th>
    fear += faceData[0].face_attributes.emotion.fear;
    # 軽蔑度</th>
    contempt += faceData[0].face_attributes.emotion.contempt;
    # 嫌悪度</th>
    disgust += faceData[0].face_attributes.emotion.disgust;
    # 中性度</th>
    neutral += faceData[0].face_attributes.emotion.neutral;

  count = len(detected_faces)
  smileScore = smile * 100 / count;
  happinessScore = happiness * 100 / count;
  angerScore = anger * 100 / count;
  sadnessScore = sadness * 100 / count;
  surpriseScore = surprise * 100 / count;
  fearScore = fear * 100 / count;
  contemptScore = contempt * 100 / count;
  disgustScore = disgust * 100 / count;
  neutralScore = neutral * 100 / count;
  
  positiveScore = round((happinessScore * 10) + (neutralScore * 5));
  negativeScore = round((angerScore * 2) + (sadnessScore * 2) + (fearScore * 2) + (contempt * 5) + (disgustScore * 10)) ;
  
  TotalScore = positiveScore - negativeScore;

   
  ret = {
    'smile': smile,
    'happiness': happiness,
    'anger': anger,
    'sadness': sadness,
    'surprise': surprise,
    'fear': fear,
    'contempt': contempt,
    'disgust': disgust,
    'neutral': neutral,
    'positive': positiveScore,
    'negative': negativeScore,
    'total': TotalScore,
  } 
  
  return ret
    
  
  