
from django.shortcuts import render
from django.http import HttpResponseRedirect

from manage_users.models import Users, UserForm


#def index(request):
	#users_list = Users.objects.order_by('-user_last_name')
	#context = {'users_list': users_list}
	#return render(request, 'home.html', context)

def index(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			first_name = request.POST.get('first_name', '')
			last_name = request.POST.get('last_name', '')
			email = request.POST.get('email', '')
			users_obj = Users(user_first_name=first_name, user_last_name=last_name, email_address=email)
			return HttpResponseRedirect('/')
	else:
		form = UserForm()
	return render(request, 'home.html', {
		'form': form,
		})




