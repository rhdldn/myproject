import requests
import json
import datetime
from django.utils.timezone import make_aware
from . import commonUtil
from . import models

#매치 정보 조회
def getLstMatchInfo(rankList, userId, accountId, apiKey):        
    print("매치 정보 조회")

    ##매치 정보 조회 API
    params = {'beginIndex': 0, 'endIndex': 8}
    r = requests.get(commonUtil.apiUrl + "lol/match/v4/matchlists/by-account/"+ accountId +"?api_key="+ apiKey, params)
    matchJson = r.json()

    #print(matchJson)
    parsingMatchInfo(matchJson, userId, accountId, apiKey)

#매치 정보 파싱
def parsingMatchInfo(matchJson, userId, accountId, apiKey):
    print("매치 정보 파싱")

    matchList = matchJson['matches']
    for matchInfo in matchList: 
        conv_game_time = make_aware(datetime.datetime.fromtimestamp(matchInfo['timestamp']/1000))
        conv_game_time = datetime.datetime.strftime(conv_game_time, "%Y-%m-%d %H:%M:%S")
        models.LUserMatch.objects.filter(user_game_id=userId, game_match_id=matchInfo['gameId']).update(champion_id=matchInfo['champion'], que_type=matchInfo['queue'], season=matchInfo['season'], game_date=conv_game_time, game_role=matchInfo['role'], lane=matchInfo['lane'], upd_date=datetime.datetime.now())
        parsingMatchDetail(userId, accountId, matchInfo['gameId'], apiKey)     

#매치 상세 정보 파싱
def parsingMatchDetail(userId, accountId, gameId, apiKey):
    print("매치 상세 정보 파싱")

    ##매치 상세 정보 조회 API
    r = requests.get(commonUtil.apiUrl + "lol/match/v4/matches/"+ str(gameId) +"?api_key="+ apiKey)
    matchDtlJson = r.json()

    if matchDtlJson['participantIdentities'] != None :
        matchUserList = matchDtlJson['participantIdentities']

    for matchUserInfo in matchUserList :
        userInfo = matchUserInfo['player']
        userAccountId = userInfo['accountId']

        if accountId == userAccountId :
            participantId = matchUserInfo['participantId']

    if matchDtlJson['participants'] != None :
        matchUserDtlList = matchDtlJson['participants']
    
    for matchUserDtlInfo in matchUserDtlList :
        igParticipantId = matchUserDtlInfo['participantId']

        if participantId == igParticipantId :
            matchUserSts = matchUserDtlInfo['stats']

            winFlag = "N"

            if matchUserSts['win']:
                winFlag = "Y"

            models.LUserMatch.objects.filter(user_game_id=userId, game_match_id=gameId).update(kills=matchUserSts['kills'], deaths=matchUserSts['deaths'], assists=matchUserSts['assists'], win_flag=winFlag, upd_date=datetime.datetime.now())

            print("적재성공")