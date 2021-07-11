import random

with open("names.txt") as fhand:
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

users = 56
branch = [1,2,3]
language = ["English","Kiswahili","French","Spanish","Hindi","Chinese"]

for i in range(0,users*2,2):
    ID       = (i // 2) +1
    state    = random.choice(capitals)
    cty      = random.choice(city)
    tit      = random.choice(title)
    ski      = random.choice(skill)
    b        = random.choice(branch)
    lang     = random.choice(language)
    addr     = random.choice(address) 
    age      = f"{random.randint(21,60)}"
    n        = f"{name[i]} {name[i+1]}"
    sal      = random.randint(1000,999999)
    zipc     = random.randint(10000,99999)
    stre     = f"ST{random.randint(23,99)}"
    tel      = f"07{random.randint(10000000,99999999)}"
    doh      = f"{str(random.randint(1,28)).zfill(2)}/{str(random.randint(1,12)).zfill(2)}/{random.randint(2015,2021)}"
    formated = f"{ID},{n},{tel},{state},{cty},{zipc},{tel},{doh},{tit},{sal},{ski},{age},{b}"
    print(formated)

