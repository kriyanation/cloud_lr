from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from lessoncount import forms
from lessoncount.models import lessoncount


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            total_number_of_lessons = 10
            number_of_lessons_available = 10
            recent_payment_status = 'Free'
            new_record = lessoncount(user=user,total_number_of_lessons=total_number_of_lessons,number_of_lessons_available=number_of_lessons_available,
                                     recent_payment_status=recent_payment_status)
            lessoncount.save(new_record)

            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    lessoncounts = lessoncount.objects.filter(user=request.user.id)
    args = {
        'lessoncounts': lessoncounts
    }
    if request.method == 'POST':

        print("button clicked")

    return render(request, 'home.html',args)