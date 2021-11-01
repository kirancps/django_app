from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):

    return render(request,'users/home.html')



def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('login-page')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    context = {
        'posts': User.objects.all()
                 }

    return render(request,'users/profile.html',context)