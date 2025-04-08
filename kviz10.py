cisla = [1,2,-2,-2,1]
kladna = 0
zaporna = 0
for c in cisla:
    if c>0:
        kladna= kladna +1
    elif c<0:
        zaporna = zaporna +1 
print(f"{kladna} kla a {zaporna} zap")
