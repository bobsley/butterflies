import datetime

from django.db import models
from django.utils import timezone

class ListOfButterflies(models.Model):
	name = models.CharField(max_length=24, help_text=u'name')
	family = models.CharField(max_length=24)
	subfamily = models.CharField(max_length=24)
	habitat = models.CharField(max_length=50)
	description = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published', blank=True)

	def __str__(self):
		return self.name

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)