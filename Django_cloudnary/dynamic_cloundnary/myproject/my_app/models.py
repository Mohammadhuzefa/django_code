from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage,RawMediaCloudinaryStorage,VideoMediaCloudinaryStorage
# filefield for all
# Create your models here.

# class Stu(models.Model):
#     img=models.ImageField(null=True,upload_to='img/')
#     audio=models.FileField(null=True,upload_to='aud/')
#     video=models.FileField(null=True,upload_to='vid/')


class Stu(models.Model):
		image = models.ImageField(null=True,upload_to='img/',storage=MediaCloudinaryStorage)
		audio = models.FileField(null=True,upload_to='aud/',storage=VideoMediaCloudinaryStorage)
		video = models.FileField(null=True,upload_to='vid/',storage=VideoMediaCloudinaryStorage)
		