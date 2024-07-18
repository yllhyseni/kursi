#def hello():
#    print("hello world")
#rezultati = 0
#def katror(x):
#    rezultati = x**2
#    return rezultati
#y= katror(5) + 5 
#print(y)

#shuma = 0
#prodhimi = 0

#def calculate(x, y, o):
#    if o == "+":
 #       shuma = x + y
#        return shuma
 #   elif o == "*":
 #       prodhimi = x * y
  #      return prodhimi
   # else:
  #      print("numri ose operatori nuke eshte valid")


#result = calculate(1, 3, "+")
#print(result)

#result = calculate(1, 3, "*")
#print(result)

numra = [3, 6, 9, 11]


numra_min = 0
numra_max = 0
shuma_e_numrave = 0
mesatarja_e_numrave = 0

def find_min():
    global numra_min
    numra_min = min(numra)
    return numra_min

def find_max():
    global numra_max
    numra_max = max(numra)
    return numra_max

def calculate_sum():
    global shuma_e_numrave
    shuma_e_numrave = sum(numra)
    return shuma_e_numrave

def calculate_average():
    global mesatarja_e_numrave
    mesatarja_e_numrave = sum(numra) / len(numra)
    return mesatarja_e_numrave


find_min()
find_max()
calculate_sum()
calculate_average()

print(f"Minimum value: {numra_min}")
print(f"Maximum value: {numra_max}")
print(f"Sum of numbers: {shuma_e_numrave}")
print(f"Average of numbers: {mesatarja_e_numrave}")