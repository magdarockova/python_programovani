# SyntaxError (něco chybí/přebývá)

# vek = int(input("Zadej věk: "))
# if vek > 15
#     print("Vítej")

#IndentationError = odsazení chybí/přebývá

# vek = int(input("Zadej věk: "))
# if vek > 15:
# print("Vítej")

#TypeError 
# vek = input("Zadej věk: ")
# if vek > 15:
#     print("Vítej")

#NameError
# promenna = 10
# print(promenna)  # vypíše 10
# print(promena)   # chyba v programu

#ValueError
# vek = int(input("Zadej věk: "))
# if vek > 15:
#     print("Vítej")

#IndexError - pracujeme se sekvencí a jsme mimo rozsah toho, pro co mám hodnoty
# knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]
# index = int(input("Zadej index knihy: "))
# print(knihy[index])

#KeyError
# zvirata = {'dog': 'pes', 'cat': 'kočka'}
# klic = input("Zadej zvíře pro překlad: ")
# print(zvirata[klic])


#AssertionError 
# def is_odd(number):
#     return number % 2 == 0
# # 4 % 2 -> 0 -> is_odd vrátí True
# # 5 % 2 -> 1 -> id_odd vrátí False
# # funkce is_odd by měla vrátit True pro liché číslo a False pro sudé
# # odd = liché, even = sudé
# # od funkce očekávám, že pro číslo 4 vrátí False
# assert is_odd(4) == False
# assert is_odd(5) == True

##Ve správné verzi programu by totiž měla funkce vypadat takto:
# def is_odd(number):
#     return number % 2 == 1

