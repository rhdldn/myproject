from django.urls import path

from . import views

urlpatterns = [
    path('userlist/<str:userId>', views.userDtlList, name='userlist'),
    path('userlist', views.userList, name='userlist'),
    path('ponylist', views.ponyList, name='ponylist'),
    path('ponylist/<str:userId>', views.ponyStsUpdList, name='ponyStsUpdList'),
    path('enemylist', views.enemyList, name='enemylist'),
    path('enemylist/<str:userId>', views.enemyStsUpdList, name='enemyStsUpdList'),    
    path('updkey/<str:apiKey>', views.updKey, name='updKey'),
    path('statlist', views.newFow, name='ponylist'),
]