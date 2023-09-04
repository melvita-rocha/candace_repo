from django.db import models

# Create your models here.
class Blog(models.Model):
	id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=255)
	pub_date= models.DateTimeField()
	body= models.TextField()
	img= models.ImageField(upload_to='images/')
