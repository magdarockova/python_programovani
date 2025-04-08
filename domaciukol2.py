## CAST 1

import requests
ico = input("Zadej IČO subjektu: ")

def get_ares_ico(ico):
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    response = requests.get(url)
    
    try:
        data = response.json()
        #print(data)   -- kontrola dat z api
        business_name = data.get('obchodniJmeno')
        address = data.get('sidlo', {}).get('textovaAdresa')
        
        if business_name and address:
            print(f"{business_name}\n{address}")
        else:
            print("Nelze nalézt informace o subjektu.")
    except requests.exceptions.RequestException:
        print("Chyba při zpracování dat.")

get_ares_ico(ico)

## Bonus

def get_ciselnik_pravni_forma():
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"
    
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    
    data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
    response = requests.post(url, headers=headers, data=data)

    try:
            data = response.json()
            ciselniky = data.get('ciselniky', [])
            if ciselniky:
                ciselnik = ciselniky[0].get('polozkyCiselniku', [])
                return ciselnik
            else:
                print("Číselník nebyl nalezen.")
                return []
    except:
        print("Došlo k chybě při zpracování číselníku.")
        return []

def get_pravni_forma(kod, pravni_forma):
    for item in pravni_forma:
        if item.get('kod') == kod:
            return item.get('nazev')
    return "Neznámá právní forma"


## CAST 2
nazev = input("Zadej název subjektu: ")

def get_ares_nazev(nazev, pravni_forma):
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
    
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    
    data = f'{{"obchodniJmeno": "{nazev}"}}'
    response = requests.post(url, headers=headers, data=data)
    
    try:
        data = response.json()
        pocet_celkem = data.get('pocetCelkem', 0)
        print(f"Nalezeno subjektů: {pocet_celkem}")
        
        ekonomicke_subjekty = data.get('ekonomickeSubjekty', [])
        
        if ekonomicke_subjekty:
            for subjekt in ekonomicke_subjekty:
                obchodni_jmeno = subjekt.get('obchodniJmeno')
                ico = subjekt.get('ico')
                pravni_forma_kod = subjekt.get('pravniForma')
                pravni_forma_jmeno = get_pravni_forma(pravni_forma_kod, pravni_forma)
                print(f"{obchodni_jmeno}, {ico}, {pravni_forma_jmeno}")
        else:
            print("Žádné subjekty nebyly nalezeny.")
    except requests.exceptions.RequestException:
        print("Chyba při zpracování dat.")

pravni_forma = get_ciselnik_pravni_forma()
get_ares_nazev(nazev, pravni_forma)

