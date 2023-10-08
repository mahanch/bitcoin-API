import requests
api = 'a583af9e9d6a8f76'
response = requests.get('https://coinlib.io/api/v1/global?key=%s&pref=USD'% api)

print(response.json().["coins"])
