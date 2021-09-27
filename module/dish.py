import requests
import json


def dish_from_date(ymd, sc):
    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'

    params = {
        'Type': 'json',
        
        'ATPT_OFCDC_SC_CODE': 'P10',
        'SD_SCHUL_CODE': '8320093',
        'MMEAL_SC_CODE': sc,
        'MLSV_YMD': ymd
    }

    res = requests.get(url, params=params).json()

    try:
        dishes=res['mealServiceDietInfo'][1]['row'][0]['DDISH_NM'].split('<br/>')

        return dishes
    except:
        errormessage=res['RESULT']['MESSAGE'];
        
        return [errormessage]