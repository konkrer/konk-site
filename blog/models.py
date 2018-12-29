from django.db import models

class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	pub_date = models.DateField()
	body = models.TextField()

	def summary(self):
		return self.body[:100]

	def date_pretty(self):
		return str(self.pub_date) + " in the shit universe"

	def __str__(self):
		return self.title