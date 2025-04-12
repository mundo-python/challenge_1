import requests 
from bs4 import BeautifulSoup 
import time
import json 

url = "https://www.kavak.com/mx/seminuevos/coupe?page=0"
response = requests.get(url)
if response.status_code != 200: 
	print(f"Error con code {response.status_code}")

paginas = 6
coupes = []

for pagina in range(paginas):
	url_salto = url + str(pagina)
	print(f"Consultando: {url_salto}")

	respuesta = requests.get(url_salto)
	soup = BeautifulSoup(respuesta.text, "html.parser")

	auto_tag = soup.find_all("h3", class_ = "card-product_cardProduct__title__RR0CK")
	info_tag = soup.find_all("p", class_ = "card-product_cardProduct__subtitle__hbN2a")
	precio_tag = soup.find_all("span", class_ = "amount_uki-amount__large__price__2NvVx")

	for a, info, precio, in zip(auto_tag, info_tag, precio_tag):
		auto = a.text.strip()
		partes_info = info.text.strip().split(" • ")
		año = partes_info[0]
		kilometraje = partes_info[1]
		precio = precio.text.strip()
		precio_clean = precio.replace("$", "").replace(",", "").strip()
		precio_num = int(precio_clean)

		coupes.append(
			{"modelo": auto,
			"año": año,
			"kilometraje": kilometraje,
			"precio": precio,
			"precio_num": precio_num
			})

coupes_ordenados = sorted(coupes, key=lambda x: x["precio_num"])

with open("coupes.json", "w", encoding = "utf-8") as f:
	json.dump(coupes_ordenados, f, ensure_ascii = False, indent = 4)
