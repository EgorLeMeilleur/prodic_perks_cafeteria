from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from Benefits.models import Benefit, Purchase, Wish
from Worker.forms import LoginForm
from django.urls import reverse


def beginning_page(request):
    return render(request, 'index.html')


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
    user = request.user
    if user.profile.position == 'hr':
        return render(request, 'logged_hr.html')
    else:
        return render(request, 'logged_worker.html')
    # bought_benefits = Purchase.objects.filter(user=user)
    # param = {'benefits': benefits, 'bought_benefits': bought_benefits, 'wished_benefits': wished_benefits}


@login_required
def wished_show(request):
    user = request.user
    wished_benefits = Wish.objects.filter(user=user)
    return render(request, 'wished_benefits.html', {'benefits': wished_benefits})


@login_required
def benefits_show(request):
    user = request.user
    benefits = Benefit.objects.filter(city=user.profile.city)
    return render(request, 'benefits.html', {'benefits': benefits})


@login_required
def bought(request, pk):
    user_id = request.user
    benefit = get_object_or_404(Benefit, pk=pk)
    if user_id.profile.balance >= benefit.price:
        user_id.profile.balance -= benefit.price
        new_obj = Purchase(user=user_id, benefit=benefit)
        if Wish.objects.filter(user=user_id, benefit=benefit).exists():
            Wish.objects.filter(user=user_id, benefit=benefit).delete()
        new_obj.save()
        user_id.save()
    return redirect('personal_cabinet')


@login_required
def wished(request, pk):
    user_id = request.user
    benefit = get_object_or_404(Benefit, pk=pk)
    if not Wish.objects.filter(user=user_id, benefit=benefit).exists():
        new_obj = Wish(user=user_id, benefit=benefit)
        new_obj.save()
    return redirect('personal_cabinet')


@login_required
def wished_remove(request, pk):
    user_id = request.user
    benefit = get_object_or_404(Benefit, pk=pk)
    Wish.objects.filter(user=user_id, benefit=benefit).delete()
    return redirect('personal_cabinet')


@login_required
def delete_benefit(request, pk):
    Benefit.objects.filter(pk=pk).delete()
    return redirect('personal_cabinet')


@login_required()
def delete_worker(request, pk):
    User.objects.get(pk=pk).delete()
    return redirect('personal_cabinet')


# @login_required
# def sort_by_(request):
#     return redirect(reverse('home'))


@login_required
def logout(request):
    return redirect('home')
