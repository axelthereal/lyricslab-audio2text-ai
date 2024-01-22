from django.db import models

class Media(models.models):
    title = models.CharField(max_length=255)
    media_file = models.FileField(upload_to='media/')