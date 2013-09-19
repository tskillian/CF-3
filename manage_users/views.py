
from django.shortcuts import render
from django.http import HttpResponseRedirect

from manage_users.models import Users, UserForm

def index(request):
	first_names = []
	last_names = []
	emails = []
	for i in Users.objects.all():
		first_names.append(i.user_first_name)
		last_names.append(i.user_last_name)
		emails.append(i.email_address)

	current_users = []
	for i in len(first_names):
		current_users.append(" ".join([first_names[i], last_names[i], emails[i][]))

	index = len(first_names)-1

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			users_obj = form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserForm()
	return render(request, 'home.html', {
		'form': form, 'first_names': first_names,
		'last_names': last_names, 'emails': emails,
		'index': index, 'current_users': current_users
		})




