
from django.shortcuts import render

from manage_users.models import Users


def index(request):
	users_list = Users.objects.order_by('-user_last_name')
	context = {'users_list': users_list}
	return render(request, 'home.html', context)

