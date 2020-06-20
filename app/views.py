from django.shortcuts import render
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login
from .forms import *
from django.http import JsonResponse
from datetime import timedelta
import datetime


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


def plan(request):
    return render(request, 'app/plan.html')


class ProfileView(View):
    template_name = 'app/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        amount = request.POST.get('amount')
        interest = request.POST.get('interest')
        total = request.POST.get('total')
        user = User.objects.get(username=request.user.username)
        current_date = datetime.datetime.now()
        try:
            oldUser = Plan.objects.filter(is_new=False).update(
                user=user,
                amount=amount,
                interest=interest,
                total=total,
                start_date=current_date,
                end_date=current_date + timedelta(days=7),
                duration=7
            )
        except Plan.DoesNotExist:
            Plan.objects.create(
                user=user,
                amount=amount,
                interest=interest,
                total=total,
                start_date=current_date,
                end_date=current_date + timedelta(days=3),
                duration=3
            )
        return render(request, self.template_name,)
