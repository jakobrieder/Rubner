import random

daten = [random.randint(0, n) for n in range(1, 100)]
print(daten)


def nonunique(daten):
    count = 0
    nonuniqueValues = []
    for n in daten:
        if daten.count(n) >= 2 and n not in nonuniqueValues:
            nonuniqueValues.append(n)
            count = count + 1
    return count



print(nonunique(daten))
print(len(daten))

d = {}
for n in daten:
    d[n] = 0
daten = list(d.keys())

print(nonunique(daten))
print(len(daten))
print(daten)




