from django.db import models

# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=255)
    media_file = models.FileField(upload_to='cloud')

    def __str__(self):
        return self.title