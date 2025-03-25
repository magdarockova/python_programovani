""" 
Zadání
Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí.
Aplikace bude postavená na principech OOP. Tato daň se vztahuje na pozemky, bytové a komerční prostory.
Výše daně se odvíjí od několika faktorů, např. typu nemovitosti, velikosti, lokalitě, kde se nemovitost nachází atd.
"""

import math
from abc import ABC, abstractmethod


# trida Locality, atributy name a locality_coefficient
class Locality:            
    def __init__(self, name, locality_coefficient):       
        self.name = name
        self.locality_coefficient = locality_coefficient
        
    def get_info(self):                                             
        return f"Nemovitost se nachází v katastru {self.name} a koeficient činí {self.locality_coefficient}."

# trida Property, atribut locality musí být instance třídy Locality
class Property(ABC):             
    def __init__(self, locality):
        if not isinstance(locality, Locality):
            print("Atribut locality musí být instance třídy Locality.")
        self.locality = locality
    
    @abstractmethod
    def calculate_tax(self):
        pass

    @abstractmethod
    def __str__(self):
        pass      

# trida Estate, která je potomkem třídy Property, atributy locality, estate_type, area
class Estate(Property):     
    ESTATE_TYPE_COEFFICIENT = {
        "zemědělský pozemek": 0.85,
        "stavební pozemek": 9,
        "les": 0.35,
        "zahrada": 2
    }

    def __init__(self, locality, estate_type, area):
        super().__init__(locality)           
        if estate_type not in self.ESTATE_TYPE_COEFFICIENT:
            print(f"Neplatný ty pozemku. Musí obsahovat: {list(self.ESTATE_TYPE_COEFFICIENT.keys())}.")
        self.estate_type = estate_type
        self.area = area

    # Metoda calculate_tax, která vrací zaokrouhlenou hodnotu daně
    def calculate_tax(self):
        estate_coefficient = self.ESTATE_TYPE_COEFFICIENT[self.estate_type]
        tax = self.area * estate_coefficient * self.locality.locality_coefficient
        return math.ceil(tax)
    # bonus str Např.: Zemědělský pozemek, lokalita Manětín (koeficient 1), 900 metrů čtverečních, daň 765 Kč.
    def __str__(self):
        tax = self.calculate_tax()
        return f"{self.estate_type}, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {tax} Kč."

lokalita1 = Locality("lokalita1", 2)
estate1 = Estate(lokalita1, "les", 500)  
'''
# vypocet lesni
tax = estate1.calculate_tax()
print(f"Tax for the estate is: {tax}")
'''

class Residence(Property):          #trida Residence (byt, dům, jina stavba) a je potomkem tridy Property + atributy locality, area (podlahová plocha) a commercial (bool)
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial == True:
            return tax * 2
        else: return tax
    def __str__(self):
        tax = self.calculate_tax()
        if self.commercial:
            return f"Komerční nemovitost, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {tax} Kč."
        else:
            return f"Nekomerční nemovitost, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {tax} Kč."
    
    
lokalita2 = Locality("lokalita2", 3)
byt = Residence(lokalita2, 60, False)
kancl = Residence(lokalita2, 60, True)
'''
# vypocet byt
print(byt.calculate_tax())
print(kancl.calculate_tax())

'''
Manetin = Locality("Manetin", 0.8)
zemedelsky_pozemek = Estate(Manetin, "zemědělský pozemek", 900)
print(zemedelsky_pozemek.calculate_tax())
dum = Residence(Manetin, 120, False)
print(dum.calculate_tax())
Brno = Locality("Brno", 3)
kancelar = Residence(Brno, 90, True)
print(kancelar.calculate_tax())

print(zemedelsky_pozemek.__str__())
print(dum.__str__())

