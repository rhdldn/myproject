from django.http import HttpResponse
from django.template import loader
from . import lolStsService
from . import lolAddStsService
from . import lolApiKeyService
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

    resultVal = lolStsService.getLolRank(userId, "")

    context = {
        'resultVal': resultVal,
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

def ponyStsUpdList(request, userId):
    template = loader.get_template('lolapp/ponylist.html')

    lolAddStsService.createUserHs(userId)

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

def enemyStsUpdList(request, userId):
    template = loader.get_template('lolapp/enemylist.html')
    
    lolAddStsService.createUserHs(userId)

    resultVal = lolStsService.getLolRank("", "ENERMY")

    context = {
        'resultVal': resultVal,
    }
    return HttpResponse(template.render(context, request))

def updKey(request, apiKey):
    template = loader.get_template('lolapp/userlist.html')

    lolApiKeyService.modifyApiKey(apiKey)

    context = {
        'resultVal': "갱신되었습니다.",
    }
    return HttpResponse(template.render(context, request))

def newFow(request):
    template = loader.get_template('lolapp/statlist.html')
    context = {
        'dd': "Hello",
    }
    return HttpResponse(template.render(context, request))

