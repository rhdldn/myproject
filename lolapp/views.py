from django.http import HttpResponse
from django.template import loader
from . import lolStsService
from . import lolAddStsService
from . import models

def userList(request):
    template = loader.get_template('lolapp/userlist.html')
    context = {
        'dd': "Hello",
    }
    return HttpResponse(template.render(context, request))

def userDtlList(request, userId):
    template = loader.get_template('lolapp/userlist.html')

    lolAddStsService.createUserHs(userId)

    context = {
        'dd': "Hello",
    }
    return HttpResponse(template.render(context, request))

def ponyList(request):
    template = loader.get_template('lolapp/ponylist.html')

    resultVal = lolStsService.getLolRank("", "PONY")

    #print(resultVal)
    context = {
        'resultVal': resultVal,
    }
    return HttpResponse(template.render(context, request))

def enemyList(request):
    template = loader.get_template('lolapp/enemylist.html')

    resultVal = lolStsService.getLolRank("", "ENERMY")
    context = {
        'resultVal': resultVal,
    }
    return HttpResponse(template.render(context, request))