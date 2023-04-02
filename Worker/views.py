from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from Benefits.models import Benefit, Purchase, Wish
from Worker.forms import LoginForm
from django.urls import reverse


def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('personal_cabinet'))
            else:
                form.add_error(None, 'Incorrect username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def personal_cabinet(request):
    benefits = Benefit.objects.all()
    bought_benefits = Purchase.objects.filter(user=request.user.profile)
    wished_benefits = Wish.objects.filter(user=request.user.profile)
    param = {'benefits': benefits, 'bought_benefits': bought_benefits, 'wished_benefits': wished_benefits}
    return render(request, 'logged.html', {'param': param})

@login_required
def bought(request, pk):
    user_id = request.user.profile
    benefit = get_object_or_404(Benefit, pk=pk)
    if user_id.balance >= benefit.price:
        user_id.balance -= benefit.price
        new_obj = Purchase(user=user_id, benefit=benefit)
        if benefit in Wish.objects.all():
            Wish.delete(benefit)
        new_obj.save()
        user_id.save()
    return redirect('personal_cabinet')


@login_required
def wished(request, pk):
    user_id = request.user.profile
    benefit = get_object_or_404(Benefit, pk=pk)
    new_obj = Wish(user=user_id, benefit=benefit)
    new_obj.save()
    return redirect('personal_cabinet')


@login_required
def logout(request):
    return redirect(reverse('home'))
