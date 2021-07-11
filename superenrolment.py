import random

norders = 13

for i in range(1,norders+1):
    superid  = random.randint(1,4)
    itemid   = random.randint(1,35)
    doo      = f"{str(random.randint(1,28)).zfill(2)}/{str(random.randint(1,12)).zfill(2)}/{random.randint(2015,2021)}"
    formated = f"{superid},{itemid},{doo}"
    print(formated)

