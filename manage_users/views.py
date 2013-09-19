
from django.shortcuts import render
from django.http import HttpResponseRedirect

from manage_users.models import Users, UserForm

def index(request):
	users_list = []
	for i in Users.objects.all():
		users_list.append(i.user_first_name)
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			users_obj = form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserForm()
	return render(request, 'home.html', {
		'form': form, 'users_list': users_list
		})




