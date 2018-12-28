from django.db import models

class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	#pub_date = models.DateField(default='1975-04-03')
	body = models.TextField()

