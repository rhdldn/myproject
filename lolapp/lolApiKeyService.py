from . import commonUtil
from . import models

def modifyApiKey(apiKey):
        
    if apiKey != None and apiKey != '':

        apiKeyModel = models.LApikey.objects.all()
        apiKeyModel.update(api_key=apiKey)
        print("APIKEY 갱신 성공")

