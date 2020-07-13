import requests
import json
import datetime
import pandas as pd
from . import models
from . import commonUtil
from . import lolRankService

#유저 전적 등록/갱신
def createUserHs(userId):
    
    ##API KEY DB 조회
    apiKeyModel = models.LApikey.objects.all()

    for apiKeyInfo in apiKeyModel:
        apiKey = apiKeyInfo.api_key
        print(apiKey)
    
    ##유저 정보 조회 API
    r = requests.get(commonUtil.apiUrl + "lol/summoner/v4/summoners/by-name/"+ userId +"?api_key="+ apiKey)
    userJson = r.json()
    print(userJson)
    userJson['userId'] = userId
    userJson['userType'] = ""
    
    #유저 정보 갱신
    try:
        userModel = models.LUser.objects.get(user_game_id=userId)
        userModel.game_lvl = userJson['summonerLevel']
        userModel.euc_id = userJson['id']
        userModel.account_id = userJson['accountId']
        userModel.puuid = userJson['puuid']
        userModel.upd_date = datetime.datetime.now()
        userModel.save()

    except models.LUser.DoesNotExist:
        userModel = models.LUser(user_game_id=userId, user_type=userJson['userType'], game_lvl=userJson['summonerLevel'], euc_id=userJson['id'], account_id=userJson['accountId'], puuid=userJson['puuid'], reg_date=datetime.datetime.now(), upd_date=datetime.datetime.now())
        userModel.save()

    userModel = models.LUser.objects.filter(user_game_id=userId)

    # if userId != None :
    #     userModel = models.LUser.objects.filter(user_game_id=userId)
    # else :
    #     print("유저 정보 없음")

    lolRankService.getRankInfo(userId, userModel, apiKey)