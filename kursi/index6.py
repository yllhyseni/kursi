country = ["kosovo", "germany", "switzerland", "albania", "usa"]

for i in country:
    print(i)

country.append("italy")

del country[2]

print(country[3])

sorted_country = sorted(country)
print(sorted_country)