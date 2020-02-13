from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages


def loginPage(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
	else:
		form = AuthenticationForm()
	return render(request , 'login.html',{"form":form})