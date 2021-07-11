import random

with open("names.txt") as f:
    names = f.read().strip().split("\n")
with open("address.txt") as f:
    addresses = f.read().strip().split("\n")
with open("city.txt") as f:
    cities = f.read().strip().split("\n")
with open("specializations.txt") as f:
    specialties = f.read().strip().split("\n")
with open("lawz.txt") as f:
    barz = f.read().strip().split("\n")

noatton = 30


for i in range(1,30*2,2):
    address = random.choice(addresses)
    name    = names[i] +' ' + names[i+1]
    city    = random.choice(cities)
    zip     = random.randint(10000,99999)
    speacial= random.choice(specialties)
    bar     = random.choice(barz) 

    formatted = f"{name},{address},{city},{zip},{speacial},{bar}"
    print(formatted)
