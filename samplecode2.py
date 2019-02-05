import requests

base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
city = '神戸'
city_code = '280010'

target_url = base_url + '?city=' + city_code
headers = {'content-type':'application/json'}
res = requests.get(target_url, headers=headers)
data = res.json()
forecast = data['forecasts'][1]



print('{0}の{1}の天気は{2}、最高気温は{3}℃です。'.format(
    data['location']['city'],  # 都市
    forecast['dateLabel'],  # 予報日
    forecast['telop'],  # 天気
    forecast['temperature']['max']['celsius']))  # 最高気温（摂氏）


