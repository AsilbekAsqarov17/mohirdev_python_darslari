import requests
from pprint import pprint

sahifa = "https://kun.uz/kr"
r = requests.get(sahifa)
pprint(r.text[:500])

country = "Uzbekistan"
url = f"https://restcountries.com/v3.1/name/{country}"
r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    pprint(data[0])
else:
    print("Xato")