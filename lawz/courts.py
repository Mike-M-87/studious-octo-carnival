import random

with open("courtnames.txt") as f:
    cnames = f.read().strip().split("\n")
with open("city.txt") as f:
    cities = f.read().strip().split("\n")
with open("capitals.txt") as f:
    states = f.read().strip().split("\n")

nocourts = 9

for i in range(nocourts):
    cid     = i + 1
    name    = cnames[i]
    city    = random.choice(cities)
    state   = random.choice(states)
    zip     = random.randint(10000,99999)

    formatted = f"{cid},{name},{city},{state},{zip}"
    print(formatted)
