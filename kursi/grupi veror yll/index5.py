#numrat = [1,3,4,6,7,9,8,24 ]
#emrat = ["yll" , "amar" , "noar"]
#emrat.append("andi")
#del emrat[0]
#emrat[0]= "jear"
#print(emrat)
#for j in emrat:
 #   print(j)
#numrat.sort()
#print(numrat)

salery = [340, 210, 450, 600, 240, 500, 550, 300]
shuma_e_pagave = 0


for i in salery:
    shuma_e_pagave += i

print(f"shuma e pagave eshte: {shuma_e_pagave}")

paga_mesatare = shuma_e_pagave / len(salery)
print(f"paga mesatare eshte: {paga_mesatare}")

#paga_min = min(salery)
#paga_max = max(salery)
#print(f"paga minimale eshte: {paga_min}")
#rint(f"paga maksimale eshte: {paga_max}")
pagaMin = salery[0]
for pagaAktuale in salery:
    if pagaAktuale < pagaMin:
        pagaMin = pagaAktuale
print(f"paga minimale eshte: {pagaMin}")
    
pagamax = salery[0]
for pagaAktuale in salery:
    if pagaAktuale > pagamax:
        pagamax = pagaAktuale
print(f"paga maksimale eshte: {pagamax}")