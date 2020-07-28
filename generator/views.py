from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	
	characters=list('abcdefghijklmnoprstuwyvxz')

	if request.GET.get('uppercase'): # w requeście znajdują się wszystkie informacje z home.html
		characters.extend(list('ABCDEFGHIJKLMNOPRSTUWVYXZ'))

	if request.GET.get('special'):
		characters.extend(list('!?+*#$'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	length=int(request.GET.get('d',12)) # 12 to wartość domyślna
	haslo=''
	for i in range(length):
		haslo+=random.choice(characters)


	return render(request, 'generator/password.html', {'password': haslo})

def info(request):
	return render(request, 'generator/info.html')