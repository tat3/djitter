from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView

from djeeterprofile.forms import SignupForm, SigninForm
from djeet.forms import DjeetForm
from users.models import User

# Views

def top_url():
    return reverse("profile:frontpage")

def return_to_top():
    topurl = top_url()
    return redirect(topurl)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "djeeterprofile/profile.html"

    def get(self, request, username):
        context = {
            "user": get_object_or_404(User, username=username),
            "form": DjeetForm()
        }
        return self.render_to_response(context)

    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        form = DjeetForm(data=request.POST)

        if form.is_valid():
            djeet = form.save(commit=False)
            djeet.user = user
            djeet.save()

        return self.render_to_response({ "form": form, "user": user, })


class FrontPageView(TemplateView):
    template_name = "djitter/frontpage.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("profile:profile", args=[request.user.username]))
        
        signupform = SignupForm()
        signinform = SigninForm()

        context = {
            "signupform": signupform,
            "signinform": signinform
        }
        return self.render_to_response(context)

    def post(self, request):
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

        context = {
            "signupform": signupform,
            "signinform": signinform
        }
        return self.render_to_response(context)


class SignoutView(LogoutView):
    next_page = "/"


class FollowsView(TemplateView):
    template_name = "djeeterprofile/users.html"

    def get(self, request, username):
        user = User.objects.get(username=username)
        djeeterprofiles = user.djeeterprofile.follows.select_related("user").all()
        return self.render_to_response({
            "title": "Follows",
            "djeeterprofiles": djeeterprofiles,
        })


class FollowersView(TemplateView):
    template_name = "djeeterprofile/users.html"

    def get(self, request, username):
        user = User.objects.get(username=username)
        djeeterprofiles = user.djeeterprofile.followed_by.select_related("user").all()
        return self.render_to_response({
            "title": "Followers",
            "djeeterprofiles": djeeterprofiles,
        })

    
class FollowView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, username):
        user = User.objects.get(username=username)
        request.user.djeeterprofile.follows.add(user.djeeterprofile)
        return HttpResponseRedirect(reverse("profile:profile", kwargs={"username": username}))


class StopFollowView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, username):
        user = User.objects.get(username=username)
        request.user.djeeterprofile.follows.remove(user.djeeterprofile)
        return HttpResponseRedirect(reverse("profile:profile", kwargs={"username": username}))

def page_not_found(request, template_name="404.html"):
    return render(request, template_name, {})

