#objekt={
 #   'emri': "yll",
 #   "mbiemri": "hyseni",
 #   "mosha": 16
#}
#key = input("shkruaje qelsin e kerkuar:")
    
#if key in objekt:
#    print("ky key eksiston")
#else:
#        print("nuk egsiston")
piket = {
    "dea": 77,
    "ereni": 81,
    "ela": 75,
    "trimi": 90,
    "rita": 100
}

shuma_e_pikeve = sum(piket.values())

num_students = len(piket)

piket_mesatare = shuma_e_pikeve / num_students

print(f"Piket mesatare te klases jane: {piket_mesatare}")