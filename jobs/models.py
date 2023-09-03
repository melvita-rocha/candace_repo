from django.db import models

# Create your models here.
class Job(models.Model):
	img= models.ImageField(upload_to='images/') #whenever uploaded where to save
	summary = models.CharField(max_length=200) #only 200 words