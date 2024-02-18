from django.urls import path, include
from . import views

app_name = 'comments'
urlpatterns = [
    path('language/<int:language_id>/add_comment_to_language/', views.add_comment_to_language, name='add_comment_to_language'),
    path('language/<int:language_id>/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
