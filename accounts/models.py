from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Phrase(models.Model):
    phrase=models.CharField(max_length=200,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.phrase


class Paid(models.Model):
    Upload_Screenshot_of_payment= CloudinaryField('image',default='')
    date_created = models.DateTimeField(auto_now_add=True)
