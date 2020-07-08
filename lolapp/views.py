from django.http import HttpResponse
from django.template import loader

def userList(request):
    template = loader.get_template('lolapp/userlist.html')
    context = {
        'dd': "Hello",
    }
    return HttpResponse(template.render(context, request))

def ponyList(request):
    template = loader.get_template('lolapp/ponylist.html')
    context = {
        'dd': "Hello",
    }
    return HttpResponse(template.render(context, request))

def enemyList(request):
    template = loader.get_template('lolapp/enemylist.html')
    context = {
        'dd': "Hello",
    }
    return HttpResponse(template.render(context, request))