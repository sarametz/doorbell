from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
	registration_id = models.CharField(max_length=200)
	user = models.ForeignKey(User)