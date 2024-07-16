#person = {
 #   "emri": "yll",
 #   "mbiemri": "hyseni",
 #   "shkolla": "don bosko",
 #   "tituli": "student",
 #   "mosha": "16"
#}


#emri = person.get("emri")
# OR
# emri = person["emri"]

#print(emri)

#erson["mosha"] = "15"

#print(person)

#for i in person:
#    print(person[i])
# OR
#for i in person.values():
 #   print(i)
 
#if "kompania" in person:
   # print("po eshte ne objekt")
#else:
  #  print("jo nuk eshte ne objekt")

#shtetet = {
    #kosova":{
     #   "kryeqyteti":"prishtina",
    #    "popullsia": 1800000000
   # },
     #"shqipria":{
      #  "kryeqyteti":"tirana",
     #   "popullsia": 455409774545
    #},
    #  "italia":{
   #      "popullsia": 5985980970867
 #   },
#}
#print(shtetet["kosova"]["kryeqyteti"])

produktet ={
    "tv": 300,
    "maus": 5,
    "laptop": 1000,
    "keybord": 50 
}
print(sorted(produktet.values()))
cmimiMeivogel = min(produktet.values())
print(f"produkti me qmimit me te vogel eshte: {cmimiMeivogel}")