# import json souboru --> python tz toho udělá slovník (viz lekce 2 a 3)

import json
with open('absolventi.json', encoding='utf-8') as file:
    absolvents = json.load(file)
print(absolvents[0])


# zapisovani do souboru json
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open('hodiny.json', mode='w', encoding='utf-8') as file:
    json.dump(hours, file, indent = 4) # nazev slovniku a potom 'file' a indent = odsazení(4mezery) --> dump vytvořit kopii

import json
data = {"řeřicha": "Česká Třebová"}

with open("data.json", mode="w", encoding="utf-8") as file1:
    json.dump(data, file1, indent = 4, ensure_ascii=False)  # soubor obsahuje {"\u0159e\u0159icha": "\u010cesk\u00e1 T\u0159ebov\u00e1"} --> \u0159e je kod pro 'ř'
#viz https://www.compart.com/en/unicode/U+0159
#ensure_ascii=False --> JSON v plném kódování UTF-8 (volitelný parametr)

################################
#Stahování dat z internetu
################################
import requests


### SEZNAM LIDI
response = requests.get('https://api.kodim.cz/python-data/people') 
data = response.json()

#1) Zjistěte kolik lidí celkem seznam obsahuje.
print(len(data))

#2) Zjistěte jaké všechny informace máme o jednotlivých osobách.
data_info = data[0].keys()
print(data_info)

#3) Zjistěte, kolik je v souboru mužů a žen
men = sum(1 for person in data if person['gender']=='Male')
print(men)
women = sum(1 for person in data if person['gender']=='Female')
print(women)

###KOČKY
response1 = requests.get('https://catfact.ninja/fact') 
cat_data = response1.json()

fact = {"fact": cat_data["fact"]}
with open('cat_fun_fact.json', mode='w', encoding='utf-8') as file:
    json.dump(fact, file, indent=4)

###SVATKY

#1) kdo ma dnes svatek
response2 = requests.get('https://svatky.adresa.info/json') 
svatek = response2.json()

print(svatek)
#print(f"Dnes má svátek: {svatek[0]['name']}")

#2) 
datum = input("Zadej datum ve formátu DDMM: ")
response3 = requests.get(f"https://svatky.adresa.info/json?date={datum}")
svatek1 = response3.json()
print(f"Tento den {datum} má svátek: {svatek1[0]['name']}")





