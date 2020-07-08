from django.urls import path

from . import views

urlpatterns = [
    path('userlist', views.userList, name='userlist'),
    path('ponylist', views.ponyList, name='ponylist'),
    path('enemylist', views.enemyList, name='enemylist'),
]