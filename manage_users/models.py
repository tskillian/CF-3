from django.db import models

class Users(models.Model):
	user_first_name = models.CharField(max_length=255)
	user_last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
