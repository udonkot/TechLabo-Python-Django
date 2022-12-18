from django.db import models

# Create your models here.
class Upload(models.Model):
  title = models.CharField(max_length=200)
 # uploaderFile = models.FileField(upload_to= "uploadFile")
  uploadBinary = models.BinaryField()
  uploadImage = models.ImageField(upload_to='uploads/')
  dateTimeOfUpdate = models.DateTimeField(auto_now= True)
  uploadFile = models.FileField(upload_to='uploads/')

class FaceInfo():
  detected_faces = any,
  faceImg = any,
  