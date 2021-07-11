import random

n  = 35
c  = 21
cl = 23
at = 30

for i in range(n):
    cid = random.randint(1,c)
    cli = random.randint(1,cl)
    att = random.randint(1,at)
    doc = f"{str(random.randint(1,28)).zfill(2)}/{str(random.randint(1,12)).zfill(2)}/{random.randint(2019,2021)}"
    form = f"{cid},{cli},{att},{doc}"
    print(form)