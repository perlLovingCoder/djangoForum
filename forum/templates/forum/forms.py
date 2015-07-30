from django import forms

#Set up the Django form class for the comment form

class CommentForm(forms.Form):
	text = models.CharField(max_length=600,default="")
	thread = models.ForeignKey(Thread)
	username = models.CharField(max_length=200)
	
#Set up the Django form class for the new thread form

class ThreadForm(forms.Form):
	title = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	description = models.CharField(max_length=600)

