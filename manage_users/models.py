from django.db import models
from django.forms import ModelForm

class Users(models.Model):
	user_first_name = models.CharField(max_length=255)
	user_last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)

class UserForm(ModelForm):
	class Meta:
		model = Users
		fields = ['user_first_name', 'user_last_name', 'email_address']