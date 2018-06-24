from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from djeeterprofile.forms import SignupForm, SigninForm
from djeet.forms import DjeetForm


# Views

def return_to_top():
    top_url = reverse("profile:frontpage")
    return redirect(top_url)

@login_required
def profile(request, username):
    user = User.objects.get(username=username)

    if request.method == 'POST':
        form = DjeetForm(data=request.POST)

        if form.is_valid():
            djeet = form.save(commit=False)
            djeet.user = request.user
            djeet.save()

        redirecturl = request.POST.get('redirect', reverse("profile:frontpage"))
        return redirect(redirecturl)
    else:
        form = DjeetForm()

    return render(request, 'djeeterprofile/profile.html', {'form': form, 'user': user})


def frontpage(request):
    if request.user.is_authenticated:
        return redirect(reverse("profile:profile", args=[request.user.username]))

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
                return return_to_top()
        else:
            signinform = SigninForm(data=request.POST)
            signupform = SignupForm()
   
            if signinform.is_valid():
                login(request, signinform.get_user())
                return return_to_top()
    else:
        signupform = SignupForm()
        signinform = SigninForm()
  
    return render(request, 'djitter/frontpage.html', {'signupform': signupform, 'signinform': signinform})


def signout(request):
    logout(request)
    return return_to_top()


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

