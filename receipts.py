import random

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

norders =  300
branch = [1,2,3]
language = ["English","Kiswahili","French","Spanish","Hindi","Chinese"]

for i in range(1,norders+1):
    itemid   = random.randint(1,35)
    quantity = random.randint(1,15)
    ID       = random.randint(1,180)
    state    = random.choice(capitals)
    cty      = random.choice(city)
    tit      = random.choice(title)
    ski      = random.choice(skill)
    b        = random.choice(branch)
    lang     = random.choice(language)
    addr     = random.choice(address) 
    age      = f"{random.randint(21,60)}"
    sal      = random.randint(1000,999999)
    zipc     = random.randint(10000,99999)
    stre     = f"ST{random.randint(23,99)}"
    tel      = f"07{random.randint(10000000,99999999)}"
    doo      = f"{str(random.randint(1,28)).zfill(2)}/{str(random.randint(1,12)).zfill(2)}/{random.randint(2015,2021)}"
    credAuts = random.randint(0,1)
    formated = f"{ID},{itemid},{quantity}"
    print(formated)

