import random

with open("names.txt") as fhand:
    name = (fhand.read().split('\n'))

with open("city.txt") as fhand:
    city = (fhand.read().split('\n'))
  
with open("skill.txt") as fhand:
    skill = (fhand.read().split('\n'))

with open("title.txt") as fhand:
    title = (fhand.read().split('\n'))
    
Zip = 2323
telephone = "10d"
Dob ="dd/mm/yyyy"
branch = [1,3,4]
for i in range(0,112,2):
    ID = f"EM{str(i//2).zfill(2)}"
    tit = title[i//2]
    cty = city[i+1]
    state = city[i]
    n = (f"{name[i]} {name[i+1]}")
    b = random.choice(branch)
    stre = f"ST{random.randint(23,99)}"
    zipc = random.randint(10000,99999)
    sal  = random.randint(1000,999999)
    ski = random.choice(skill)
    tel  = f"07{random.randint(10000000,99999999)}"
    doh  = f"{str(random.randint(1,28)).zfill(2)}/{str(random.randint(1,12)).zfill(2)}/{random.randint(2010,2021)}"
    age  = f"{random.randint(21,60)}"
    formated = f"{ID},{n},{stre},{cty},{state},{zipc},{tel},{doh},{tit},{sal},{ski},{age},{b}"
    print(formated)
#print(len(name))

