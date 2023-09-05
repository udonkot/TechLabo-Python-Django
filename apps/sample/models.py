from django.db import models

class HazeyamaTable(models.Model):
    sample_data = models.CharField(max_length=100)

    def __str__(self):
        return self.hazeyama_data
