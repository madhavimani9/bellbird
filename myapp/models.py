from django.db import models
from django.shortcuts import HttpResponse
from django.core.exceptions import *

# Create your models here.
class Chirp(models.Model):
	text = models.CharField(max_length=140)
	votes = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.text


