with open("cases.txt") as f:
    cases = f.read().strip().split("\n")

for k,v in enumerate(cases):
    print(f"{k+1},,{v}")