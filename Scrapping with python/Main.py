from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime as dt
import os

website = "https://www.lanacion.com.ar/loterias/quiniela-nacional"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

box = soup.find('main', class_="--header-fixed-margin")

cubo = box.find('div', class_='lotteries quinielas-detail-layout row-gap-tablet-2')

numeros = cubo.find_all('span', class_='number-table-horizontal --fourxs')
numbers = []
for i in numeros:
    numero = i.get_text()
    numbers.append( '\n' + numero )
    
with open('loteria.txt','w') as file:
    file.writelines(numbers)


datos = pd.read_csv("loteria.txt")
datos.to_excel("loteria.xlsx")


# datosActuales = pd.read_excel("loteria.xlsx")
# with pd.ExcelWriter("loteria.xlsx")as writer:
#     datos.to_excel(writer, sheet_name=f"datos nuevos {dt.date.today()}")
#     datosActuales.to_excel(writer)

os.remove("loteria.txt")