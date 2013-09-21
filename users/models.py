from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)

	def __unicode__(self):
		return self.last_name

	def get_absolute_url(self):
		return reverse('user_detail', kwargs={'pk': self.pk})
