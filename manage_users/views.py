
from django.shortcuts import render
from django.http import HttpResponseRedirect

from manage_users.models import Users, UserForm


#def index(request):
	#users_list = Users.objects.order_by('-user_last_name')
	#context = {'users_list': users_list}
	#return render(request, 'home.html', context)

def index(request):
	#test = Users(user_first_name='first test', user_last_name='first test', email_address='first test')
	#test.save()
	users_list = Users.objects.all()
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user_first_name = request.POST.get('user_first_name', '')
			user_last_name = request.POST.get('user_last_name', '')
			email_address = request.POST.get('email_address', '')
			users_obj = Users(user_first_name=user_first_name, user_last_name=user_last_name, email_address=email_address)
			users_obj.save()
			return HttpResponseRedirect('/')
	else:
		form = UserForm()
	return render(request, 'home.html', {
		'form': form, 'users_list': users_list
		})




