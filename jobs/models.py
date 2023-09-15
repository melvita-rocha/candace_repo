from django.db import models

# Create your models here.
class Job(models.Model):
	id = models.AutoField(primary_key=True)
	img= models.ImageField(upload_to='images/') #whenever uploaded where to save
	summary = models.CharField(max_length=200) #only 200 words

	def __str__(self):
		return self.summary