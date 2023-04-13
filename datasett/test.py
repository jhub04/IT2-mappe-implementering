fil = open("./AirBnb-Europe.csv")
data = fil.read()
linjer = data.split("\n")

byer = {}

for linje in linjer[1:-1]:
    splittet_linje = linje.split(",")
    by = splittet_linje[0]
    if by not in byer:
        byer[by] = 0

priser = {}

for linje in linjer[1:-1]:
    splittet_linje = linje.split(",")
    pris = splittet_linje

print(byer)