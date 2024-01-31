import requests
# url='https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
url='https://api.openweathermap.org/data/2.5/weather'
api_token='3d13d45416f28b31f5935aa56040e871'
param={'q':'Minsk','appid':api_token}
response=requests.get(url,params=param)
print(response.status_code)
print(response.headers)
result=response.json()
print(result)
print(result['main']['temp_min']-272)
print(result['main']['temp_max']-272)
print(result['sys']['country'])
print(result['name'])
