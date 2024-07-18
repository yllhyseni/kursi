studentat = {}
shuma_e_numrave = 0
mesatarja_e_numrave = 0
numra_max = 0
numra_min = 0

size = int(input("Enter the length of the object: "))

for i in range(size):
    emri = input("Enter the name of the student: ")
    piket = int(input("Enter the points of the student: "))
    studentat[emri] = {'piket': piket}

def calculate_sum():
    global shuma_e_numrave
    shuma_e_numrave = sum(student['piket'] for student in studentat.values())
    return shuma_e_numrave

def calculate_average():
    global mesatarja_e_numrave
    mesatarja_e_numrave = shuma_e_numrave / len(studentat)
    return mesatarja_e_numrave

def find_min():
    global numra_min
    numra_min = min(student['piket'] for student in studentat.values())
    return numra_min

def find_max():
    global numra_max
    numra_max = max(student['piket'] for student in studentat.values())
    return numra_max

def check_pass():
    for emri, data in studentat.items():
        if data['piket'] < 60:
            studentat[emri]['ka_kaluar'] = 'Nuk ka kaluar'
        else:
            studentat[emri]['ka_kaluar'] = 'Ka kaluar'

calculate_sum()
calculate_average()
find_min()
find_max()
check_pass()

print("The dictionary is:")
print(studentat)
print(f"The sum of points is: {shuma_e_numrave}")
print(f"The average of points is: {mesatarja_e_numrave}")
print(f"The minimum points is: {numra_min}")
print(f"The maximum points is: {numra_max}")

for emri, data in studentat.items():
    print(f"Nxënësi/ja {emri} me pikë {data['piket']} {data['ka_kaluar']}")