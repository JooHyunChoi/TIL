from django.shortcuts import render

# Create your views here.

def signup(request):

    return render(request , 'accounts/signup')
def login(request):

    return render(request , 'accounts/login')
def logout(request):

    return render(request , 'accounts/signup')
