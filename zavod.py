import json
with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)
'''
print(runners[3]["jmeno"])

winner = runners[0]
winner_name = winner["jmeno"]
winner_time = winner["casy"]["oficialni"]
print(f"Vítězem se stal {winner_name} s časem {winner_time}.")
'''

#1) závod
finishers = []
for runner in runners:
    if runner['casy']['oficialni'] != 'DNF':
        finishers.append(runner['jmeno'])
        if len(finishers) > 1:
            print(f"Stříbrnou medaili získal {finishers[1]}.")
        else: print("Stříbrnou medaili nikdo nezískal.")

#2) transformace
word_dict = {}

# Otevřu si vstupní soubor a budu ho načítat v cyklu po řádcích
with open('words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        first_letter = word[0].lower()

        if first_letter not in word_dict:
            word_dict[first_letter] = [word]
        else:
            word_dict[first_letter].append(word)
for letter in word_dict:
    word_dict[letter] = sorted(word_dict[letter])

# Seřadím klíče slovníku podle abecedy
sorted_word_dict = dict(sorted(word_dict.items()))

# Výstupní slovník zapíšu do souboru ve formátu JSON, zajistím, aby byl výstup hezky odsazovaný o 4 mezery a klíče slovníku byly seřazené
with open('output.json', 'w') as json_file:
    json.dump(sorted_word_dict, json_file, ensure_ascii=False, indent=4)
