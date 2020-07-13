import json
import pandas as pd
from . import commonUtil
from . import models

#랭크 정보 조회
def getLolRank(userId, userType):

    selFlag_1 = False
    selFlag_2 = False
    retList = []    
    
    if userId != None and userId != '':
        selFlag_1 = True
    
    if userType != None and userType != '':
        selFlag_2 = True

    if selFlag_1 and selFlag_2:
        userModel = models.LUser.objects.filter(user_game_id=userId, user_type=userType)
    elif selFlag_1:
        userModel = models.LUser.objects.filter(user_game_id=userId)
    elif selFlag_2:
        userModel = models.LUser.objects.filter(user_type=userType)
    else:
        userModel = models.LUser.objects.all()
    
    print(pd.DataFrame(userModel))
    #print(pd.DataFrame(userList))

    for userInfo in userModel:

        retJson = {}
        userId = userInfo.user_game_id
        soloRankInfo = ""
        freeRankInfo = ""
        lastGameModel = ""

        #솔로 랭크 정보 조회
        soloRankModel = models.LUserRank.objects.filter(que_type="RANKED_SOLO_5x5", user_game_id=userId)    
        for soloRankInfo in soloRankModel:
            print(soloRankInfo)
        
        #자유 랭크 정보 조회
        freeRankModel = models.LUserRank.objects.filter(que_type="RANKED_FLEX_SR", user_game_id=userId)
        for freeRankInfo in freeRankModel:
            print(freeRankInfo)

        #최근 10게임 정보 조회
        lastGameModel = models.LUserMatch.objects.filter(user_game_id=userId).select_related().order_by('-game_date')[:8]

        retJson["userMap"] = userInfo
        retJson["soloRankMap"] = soloRankInfo
        retJson["freeRankMap"] = freeRankInfo
        retJson["lastGameList"] = lastGameModel    

        retList.append(retJson)

    return retList