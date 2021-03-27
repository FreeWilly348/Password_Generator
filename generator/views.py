from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	return render(request, 'generator/home.html', {'password':'123456'})
	
def password(request):
	
	thepassword = ''
	characters = list('abcdefghijklmnopqrstuvwyz')
	lenght = int(request.GET.get('lenght',12))
	
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYXZ'))
	#add special character and number
	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))
	if request.GET.get('specialcharacter'):
		characters.extend(list('!@#$%^%&*'))
	for x in range(lenght):
		thepassword += random.choice(characters)
		
	return render(request, 'generator/password.html',{'password':thepassword})