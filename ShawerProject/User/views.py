from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from .forms import RegisterForm, RegisterFormCon
from django.contrib import messages


def registerpage(request):
	return render(request, 'register.html')

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password1'])
			new_user.save()
			messages.success(
				request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح.')
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'registerpage.html', {
		'title': 'التسجيل',
		'form': form,
	})

def registercon(request):
	if request.method == 'POST':
		form = RegisterFormCon(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password1'])
			new_user.save()
			messages.success(
				request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح.')
			return redirect('login')
	else:
		form = RegisterFormCon()
	return render(request, 'registeconsolt.html', {
		'title': 'التسجيل',
		'form': form,
	})