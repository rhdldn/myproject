from django.urls import path

from . import views

urlpatterns = [
    path('userlist/<str:userId>', views.userDtlList, name='userlist'),
    path('userlist', views.userList, name='userlist'),
    path('ponylist', views.ponyList, name='ponylist'),
    path('enemylist', views.enemyList, name='enemylist'),
    path('updkey/<str:apiKey>', views.updKey, name='updKey'),
]