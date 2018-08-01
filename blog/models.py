from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

#create a class
class Post(models.Model):
	#define properties
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	#method to publish
	def pubilsh(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title