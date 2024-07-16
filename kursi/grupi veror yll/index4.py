#for i in range(11):
  #  if i == 3 or i == 6:
   #     continue
   # print(f"numrat jane: {i}")
    
#fjalia = "ai qe di me se shumti , flet me se paku!"
#sa_shkronja = 0
#for i in fjalia:
  #  if(i == "m"):
      #  sa_shkronja = sa_shkronja + 1
     #   print(f"brenda kesaj fjalie jane {sa_shkronja} m-ja")
x = int(input("shkruaje ku fillon intervali:"))
y = int(input("shkruaje ku mbaron intervali(+1):"))


for i in range(x, y, 1):
    if i % 2 == 0:
        print(f"numri: {i} eshte qift")
    else:
        print(f"numri: {i} eshte tek")


        