from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from djeeterprofile.forms import SignupForm, SigninForm
from djeet.forms import DjeetForm


# Views

def profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

        if request.method == 'POST':
            form = DjeetForm(data=request.POST)

            if form.is_valid():
                djeet = form.save(commit=False)
                djeet.user = request.user
                djeet.save()

            redirecturl = request.POST.get('redirect', '/')
            return redirect(redirecturl)
        else:
            form = DjeetForm()

        return render(request, 'djeeterprofile/profile.html', {'form': form, 'user': user})
    else:
        return redirect('/')


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/' + request.user.username + '/')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignupForm(data=request.POST)
                signinform = SigninForm()
        
                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')
            else:
                signinform = SigninForm(data=request.POST)
                signupform = SignupForm()
        
                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')
        else:
            signupform = SignupForm()
            signinform = SigninForm()
  
        return render(request, 'djitter/frontpage.html', {'signupform': signupform, 'signinform': signinform})


def signout(request):
    logout(request)
    return redirect('/')


def follows(request, username):
    user = User.objects.get(username=username)
    djeeterprofiles = user.djeeterprofile.follows.select_related("user").all()

    return render(request, 'djeeterprofile/users.html', {'title': 'Follows', 'djeeterprofiles': djeeterprofiles})

def followers(request, username):
    user = User.objects.get(username=username)
    djeeterprofiles = user.djeeterprofile.followed_by.select_related("user").all()

    return render(request, 'djeeterprofile/users.html', {'title': 'Followers', 'djeeterprofiles': djeeterprofiles})

@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    request.user.djeeterprofile.follows.add(user.djeeterprofile)

    return HttpResponseRedirect("/" + user.username + "/")

@login_required
def stopfollow(request, username):
    user = User.objects.get(username=username)
    request.user.djeeterprofile.follows.remove(user.djeeterprofile)

    return HttpResponseRedirect("/" + user.username + "/")

