from django.db import models

class Thread(models.Model):
	title = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	description = models.CharField(max_length=600)
	createdAt = models.DateField(auto_now_add=True)
	updatedAt = models.DateField(auto_now=True)
	def __str__(self):
        	return self.title

class Comment(models.Model):
	text = models.CharField(max_length=600,default="")
	thread = models.ForeignKey(Thread)
	username = models.CharField(max_length=200)
	score = models.IntegerField(default=0)
	createdAt = models.DateField(auto_now_add=True)
	updatedAt = models.DateField(auto_now=True)
	def __str__(self):
        	return self.text

