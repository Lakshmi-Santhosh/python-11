from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import TemplateView

from schoolapp.forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('schoolapp:login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)

            # Get the department parameter from the request
            selected_department = request.POST.get('department', '')

            # Redirect to new_page with the selected department parameter
            return HttpResponseRedirect('mypage.html')
        else:
            # Handle authentication failure
            pass
    return render(request, 'login.html')

def mypage(request):

        username = request.user.username
        return render(request, 'mypage.html', {'username': username})
def new_page(request):
    return render(request,'new_page.html')

def confirmation_page(request):
    return render(request,'confirmation_page.html')


