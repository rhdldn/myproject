from django.http import HttpResponse
from django.template import loader
from . import lolStsService
from . import lolAddStsService

def userList(request):
    template = loader.get_template('lolapp/userlist.html')
    context = {
        'dd': "Hello",
    }
    return HttpResponse(template.render(context, request))

def ponyList(request):
    template = loader.get_template('lolapp/ponylist.html')

    resultVal = lolStsService.getLolRank("", "PONY")

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