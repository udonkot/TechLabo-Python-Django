from django.db import models

class HazeyamaTable(models.Model):
    sample_data = models.CharField(max_length=100)

    def __str__(self):
        return self.sample_data

# class UploadedFile(models.Model):
#     file = models.FileField(upload_to='uploads/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadedFile(models.Model):
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.user
