from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home')

def signUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

def signIn(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
