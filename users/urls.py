from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('my_account/', views.account, name='my_account'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('list_users/', views.list_users, name='list_users'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('paid_card_and_free_basket/', views.paid_card_and_free_basket, name='paid_card_and_free_basket'),
    path('teacher_and_lessons/<int:user_id>/', views.teacher_and_lessons, name='teacher_and_lessons'),
]
