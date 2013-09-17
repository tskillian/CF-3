from django.conf.urls import patterns, url

from manage_users import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)
