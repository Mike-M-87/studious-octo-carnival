import random

with open("dependants.txt") as fhand:
    name = (fhand.read().split('\n'))

with open("city.txt") as fhand:
    city = (fhand.read().split('\n'))
  
with open("skill.txt") as fhand:
    skill = (fhand.read().split('\n'))

with open("title.txt") as fhand:
    title = (fhand.read().split('\n'))
    
with open("capitals.txt") as fhand:
    capitals = (fhand.read().split('\n'))

with open("address.txt") as fhand:
    address = (fhand.read().split('\n'))

users = 25
branch = [1,2,3]
relationship = ["Father","Mother","Son","Daughter","Cousin","Aunt","Sister","Brother"]

for i in range(0,users*2,2):
    empid    = random.randint(1,50)
    ID       = (i // 2) +1
    state    = random.choice(capitals)
    cty      = random.choice(city)
    tit      = random.choice(title)
    ski      = random.choice(skill)
    b        = random.choice(branch)
    addr     = random.choice(address) 
    relation = random.choice(relationship)
    age      = f"{random.randint(21,60)}"
    n        = f"{name[i]} {name[i+1]}"
    sal      = random.randint(1000,999999)
    zipc     = random.randint(10000,99999)
    stre     = f"ST{random.randint(23,99)}"
    tel      = f"07{random.randint(10000000,99999999)}"
    doh      = f"{str(random.randint(1,28)).zfill(2)}/{str(random.randint(1,12)).zfill(2)}/{random.randint(2015,2021)}"
    formated = f"{ID},{n},{age},{relation},{empid}"
    print(formated)

