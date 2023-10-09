
import requests
my_money = 4500
api = 'YOUR_API_KEY'
response = requests.get('https://coinlib.io/api/v1/global?key=%s&pref=USD'% api)

coin_price= int(response.json()["coins"])
# you can use another API to send you a SMS when ever the price was cheap enough
if coin_price <= my_money:
    print ('hey the BTC is cheap! lets buy it.')
else:
    print('not yet!')