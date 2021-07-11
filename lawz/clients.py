
import random

with open("names.txt") as f:
    names = f.read().strip().split("\n")
with open("address.txt") as f:
    addresses = f.read().strip().split("\n")
with open("city.txt") as f:
    cities = f.read().strip().split("\n")
with open("specializations.txt") as f:
    specialties = f.read().strip().split("\n")

n = 50
noatton  = 30
nocourts = 10 
bars = ["Kenya"]


for i in range(1,n*2,2):
    cliid   = (i//2)+1                                 # Coz 0 we add + 1
    name    = names[i] +' ' + names[i+1]
    address = random.choice(addresses)
    city    = random.choice(cities)
    zip     = random.randint(10000,99999)
    tel     = f"07{random.randint(10000000,99999999)}"
    special = random.choice(specialties)
    dob     = f"{str(random.randint(1,28)).zfill(2)}/{str(random.randint(1,12)).zfill(2)}/{random.randint(1930,1990)}"
    court   = random.randint(1,nocourts)

    formatted = f"{cliid},{name},{address},{city},{zip},{tel},{dob},{court}"
    
    print(formatted)
