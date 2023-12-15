import sys
FILE_NAME = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    FILE_NAME = "test_input"
with open(FILE_NAME, "r", encoding="utf-8") as f:
    r = list(map(lambda line: list(line), f.read().splitlines(keepends=False)))

universe = r[:]
for i,line in enumerate(r):
    try:
        line.index("#")
    except ValueError:
        universe.insert(i, list("."*len(r[0])))
for col in range(len(r[0])):
    for j,line in enumerate(r):
        if line[col]=="#":
            break
    else:
        for line_n, line in enumerate(r):
            universe[line_n].insert(col, ".")

for line in universe:
    print("".join(line))

galaxies = set()
for row,line in enumerate(universe):
    for col,char in enumerate(line):
        if char=="#":
            galaxies.add((row,col))

pairs = set()
for galaxy in galaxies:
    for galaxy2 in galaxies:
        if galaxy2==galaxy:continue
        if (galaxy2, galaxy) not in pairs:
            pairs.add((galaxy, galaxy2))

distances = []
for g1,g2 in pairs:
    x,y = g1
    x2,y2=g2
    dx = x2-x
    dy = y2-y
    distances.append((dx,dy,g1,g2,abs(dx+dy)+1))

print(distances)
for dist in distances:
    print(dist)

print(sum(map(lambda x: x[-1], distances)))