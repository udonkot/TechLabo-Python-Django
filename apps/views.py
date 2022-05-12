import base64
from pickle import FALSE
from django.shortcuts import render
from apps.models import Upload

from apps.main import getFaceSample

from facescore.settings import MEDIA_ROOT

# Create your views here.
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

  
    encodeData = ""
    
    print("base64:")
#    encodeData = base64.b64encode(Upload.uploadeBinary.read()).decode("ascii")
    encodeData = base64.b64encode(uploadFile.read()).decode("ascii")

    fname = MEDIA_ROOT + '/uploads/' + 'aaa.jpg'
    f = open(fname, 'wb+')
    for chunk in uploadFile.chunks():
      f.write(chunk)
    f.close
    
    ret = getFaceSample(fname)

    context = {
      'files': documents,
      'title': fileTitle,
#     'uploadfile': base64.b64encode(Upload.uploaderFile),
      'uploadfile': encodeData,
      'detected_faces': ret,
#      'img': drawFaceRectangles(),
    }

    
  else:
    context = {
      'title': "",
#      'img': drawFaceRectangles(),
    }
       
  # Uncomment this to show the face rectangles.
  # drawFaceRectangles()

  return render(request, 'apps/facescore.html', context)
