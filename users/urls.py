from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
	url(r'^$', views.UserList.as_view(), name='user_list'),
	url(r'^new$', views.UserCreate.as_view(), name='user_new'),
	url(r'^edit/(?P<pk>\d+)$', views.UserUpdate.as_view(), name='user_edit'),
	url(r'^delete/(?P<pk>\d+)$', views.UserDelete.as_view(), name='user_delete')
	)
