from django.shortcuts import render
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login
from .forms import *
from django.http import JsonResponse


def index(request):
    return render(request, 'app/index.html')


class SignUp_View(View):
    form_class = SignUpForm
    pform = ProfileForm
    initial = {'key': 'value'}
    template_name = 'app/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        pform = self.pform(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'pform': pform})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        pform = self.pform(request.POST)
        form_valid = form.is_valid()
        pform_valid = pform.is_valid()
        if form_valid and pform_valid:
            user = form.save()
            request.session['username'] = request.POST['username']
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_active = True
            user.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            raw_password = form.cleaned_data.get('password1')
            login(request, user)

            return redirect('information')
        return render(request, self.template_name, {'form': form, 'pform': pform})


def information(request):
    return render(request, 'app/information.html')


def predashaboard(request):
    return render(request, 'app/predashboard.html')


def profile(request):
    return render(request, 'app/profile.html')
