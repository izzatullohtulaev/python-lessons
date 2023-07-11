import requests

url = "https://dailyprayer.abdulrcs.repl.co/api/uzbekistan"
response = requests.get(url)
r_json = response.json()
# print(r_json)
jadval = r_json['today']
print(r_json['city'], '-', end=' ')
print(r_json['date'])
print("Namoz vaqtlari: ")
for key, value in jadval.items():
    if key=='Fajr':
        print("\tBomdod -", jadval[key])
    elif key=='Dhuhr':
        print("\tPeshin -", jadval[key])
    elif key=='Asr':
        print("\tAsr -", jadval[key])
    elif key=='Maghrib':
        print("\tShom -", jadval[key])
    elif key=="Isha'a":
        print("\tXufton -", jadval[key])