from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUSerCreationForm
from django.contrib.auth import get_user_model
from .models import User

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = CustomUSerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUSerCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def my_page(request, id):
    user_all = get_user_model()
    user_list = user_all.objects.all()
    user_info = get_object_or_404(User, id=id)
    context = {
        'user_info':user_info,
        'user_list': user_list
    }
    return render(request, 'accounts/my_page.html', context)

def follow(request, id):
    you = get_object_or_404(User, id=id) # aaa
    me = request.user # aaaa

    # if you == me:
    #     return redirect('accounts:my_page', me.id)
    if me in you.followers.all():        
        print(you.followers.all())
        you.followers.remove(me)
        print(me.followers.all())
    else:
        print(you.followers.all())
        you.followers.add(me)
        print(you.followers.all())
    return redirect('accounts:my_page', me.id)