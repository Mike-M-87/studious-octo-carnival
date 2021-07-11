import random

with open("names.txt") as f:
    names = f.read().strip().split("\n")
    
nojudge = 50
nocourts = 13


for i in range(1,nojudge+1,2):
    jid     = (i//2)+1                                
    fname   = random.choice(names) 
    lname   = random.choice(names) 
    name    = f"{fname} {lname}"
    yop     = random.randint(2004,2021)
    courtid = random.randint(1,nocourts)

    formatted = f"{jid},{name},{yop},{courtid}"
    print(formatted)

