from django.db import models


# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='pictures')
    description = models.CharField(max_length=200)
    file_type = models.CharField(max_length=256, choices=[('image', 'image'), ('thumbnail', 'thumbnail')], default='')
    owner = models.CharField(max_length=100, default='general')

   # def __str__(self):
   #     return self.name


