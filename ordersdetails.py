import random

norders =  180
branch = [1,2,3]

for i in range(1,norders+1):
    ID       = i
    b        = random.choice(branch)
    sal      = random.randint(1000,999999)
    sal      = random.randint(1000,999999)
    quant    = random.randint(1,30)
    itemid   = random.randint(1,36)
    formated = f"{ID},{b},{quant},{itemid}"
    print(formated)

