from django.urls import reverse

from paid_card.models import PaidCard
from paid_lessons.models import PaidLesson
from programming_guide.settings import DEFAULT_FROM_EMAIL
from basket.models import Basket
from programming_guide.settings import AUTH_USER_MODEL
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserEditForm, ExtendedUserCreationForm
from users.models import User
from django.core.mail import send_mail
from django.contrib.auth import logout


def send_email(subject, message, recipient_list):
    send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list)


def register(request):
    subject = 'Добро пожаловать!'
    message = 'Спасибо за регистрацию. Мы рады видеть вас в нашем сообществе.'

    if request.method != 'POST':
        form = ExtendedUserCreationForm()
    else:
        form = ExtendedUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            recipient_list = [new_user.email]
            send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list)
            return redirect(reverse('languages:index'))
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def get_inst(request):
    instagram_username = request.user.instagram if request.user.instagram else None
    if instagram_username:
        main_address = 'https://www.instagram.com/'
        full_address = main_address + instagram_username + '/'
    else:
        full_address = None
    return full_address


def get_facebook(request):
    facebook_username = request.user.facebook if request.user.facebook else None
    if facebook_username:
        main_address = 'https://www.facebook.com/'
        full_address = main_address + facebook_username + '/'
    else:
        full_address = None
    return full_address


def get_email(request):
    email_username = request.user.email if request.user.email else None
    if email_username:
        main_address = 'https://mail.google.com/mail/'
        full_address = main_address + email_username + '/0/#inbox'
    else:
        full_address = None
    return full_address


def get_linkedin(request):
    linkedin_username = request.user.linkedin if request.user.linkedin else None
    if linkedin_username:
        main_address = 'https://www.linkedin.com/in/'
        full_address = main_address + linkedin_username + '/'
    else:
        full_address = None
    return full_address


def account(request):
    user = User.objects.get(id=request.user.id)
    email = user.email
    full_address_instagram = get_inst(request)
    full_address_facebook = get_facebook(request)
    full_address_linkedin = get_linkedin(request)
    full_address_email = get_email(request)
    baskets = Basket.objects.filter(user=user)
    context = {'user': user, 'email': email, 'baskets': baskets,
               'full_address_instagram': full_address_instagram,
               'full_address_facebook': full_address_facebook,
               'full_address_email': full_address_email,
               'full_address_linkedin': full_address_linkedin,
               }
    return render(request, 'registration/account.html', context)


def edit_account(request):
    user = User.objects.get(username=request.user)
    if request.method != 'POST':
        form = UserEditForm(instance=user)
    else:
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:my_account')
    context = {'user': user, 'form': form}
    return render(request, 'registration/edit_account.html', context)


def list_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'registration/list_users.html', context)


def logged_out(request):
    logout(request)
    return redirect('languages:index')


def paid_card_and_free_basket(request):
    user = User.objects.get(id=request.user.id)
    baskets = Basket.objects.filter(user=user)
    paid_cards = PaidCard.objects.filter(user=user)
    context = {
        'baskets': baskets,
        'paid_cards': paid_cards,
    }
    return render(request, 'registration/paid-card_and_free_cards.html', context)


def teacher_and_lessons(request, user_id):
    user = User.objects.get(id=user_id)
    paid_lessons = PaidLesson.objects.filter(teacher=user_id)
    context = {'user': user, 'paid_lessons': paid_lessons}
    return render(request, 'registration/teacher_and_lessons.html', context)
