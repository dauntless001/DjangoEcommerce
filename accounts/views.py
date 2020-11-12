from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from .forms import LoginForm
from django.contrib import messages
# Create your views here.


def logout_view(request):
	logout(request)
	messages.success(request, 'Good Bye!')
	return redirect('products:home')


def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				messages.success(request, 'Welcome Back '+username)
				return redirect('products:home')
			else:
				messages.success(request, 'Oops Account Not Active')
				return redirect('accounts:login')
	name = 'login.html'
	context = {
	'form' : form
	}
	return render(request, name, context)


