import requests
import datetime
from . import models
from . import commonUtil
from . import lolMatchService

#랭크 정보 조회
def getRankInfo(userId, userModel, apiKey):
    print("랭크 정보 조회")

    for userInfo in userModel:
        eucId = userInfo.euc_id
        accountId = userInfo.account_id

    getLolUserRank(userId, eucId, accountId, apiKey)

#랭크 정보 조회 API
def getLolUserRank(userId, eucId, accountId, apiKey):
    print(eucId)

    ##랭크 정보 조회 API
    r = requests.get(commonUtil.apiUrl + "lol/league/v4/entries/by-summoner/"+ eucId +"?api_key="+ apiKey)
    rankJson = r.json()

    parsingRankInfo(rankJson)
    lolMatchService.getLstMatchInfo(rankJson, userId, accountId, apiKey)

#랭크 정보 파싱
def parsingRankInfo(rankList):
    print("랭크 정보 파싱")

    for rankInfo in rankList:        
        try:
            rankModel = models.LUserRank.objects.get(user_game_id=rankInfo['summonerName'], que_type=rankInfo['queueType'])
            rankModel.tier = rankInfo['tier']
            rankModel.rank_lvl = rankInfo['rank']
            rankModel.league_pt = rankInfo['leaguePoints']
            rankModel.wins_cnt = rankInfo['wins']
            rankModel.losses_cnt = rankInfo['losses']
            rankModel.upd_date = datetime.datetime.now()
            rankModel.save()

        except models.LUser.DoesNotExist:
            rankModel = models.LUserRank(user_game_id=rankInfo['summonerName'], que_type=userJson['queueType'], tier=userJson['tier'], rank_lvl=userJson['rank'], league_pt=userJson['leaguePoints'], wins_cnt=userJson['wins'], losses_cnt=userJson['losses'], reg_date=datetime.datetime.now(), upd_date=datetime.datetime.now())
            rankModel.save()