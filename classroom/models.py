from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
import uuid

# Create your models here.

class Classroom(models.Model):
	"""
	Classrooms with max capability of 10 students
	"""
	uuid = models.UUIDField(default = uuid.uuid4)
	name = models.CharField(max_length = 100)
	description = models.TextField(default = "")
	admin = models.ForeignKey(User)

	def __str__(self):
		return str(self.name)


class Student(models.Model):
	"""
	Student Account
	"""
	user = models.ForeignKey(User)
	classroom = models.ForeignKey(Classroom)

	def __str__(self):
		return  str(self.user.first_name) + str(self.user.last_name)


