
def deleni1():
    # Získáme první číslo od uživatele
    cislo1 = float(input("Zadej první číslo: "))
    # Získáme druhé číslo od uživatele
    cislo2 = float(input("Zadej druhé číslo: "))
    
    # Ověříme, zda nedochází k dělení nulou
    if cislo2 == 0:
        print("Dělení nulou není možné.")
    else:
        # Vypočítáme výsledek dělení
        vysledek = cislo1 / cislo2
        print(f"Výsledek je {vysledek}")

print(deleni1())


knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]

index = int(input("Zadej index knihy: "))
print(knihy[index])



