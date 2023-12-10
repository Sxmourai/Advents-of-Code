import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input2"
with open(file_name, "r") as f:
    steps = f.readline()
    f.readline()
    r = f.read()
step_pos = 0
wasteland_map = {}
for line in r.splitlines(keepends=False):
    src,dests = line.split(" = ")
    left,right = dests[1:-1].split(", ")
    wasteland_map[src] = left,right

srcs = set(filter(lambda x: x.endswith("A"), wasteland_map.keys()))
i=0
while srcs:
    for src in srcs.copy():
        left,right = wasteland_map[src]
        srcs.remove(src)
        src = right
        if steps[step_pos%(len(steps)-1)]=="L":
            src = left
        srcs.add(src)
    # print(srcs)
    step_pos+=1
    for src in srcs: # Check if they all end with Z
        if not src.endswith("Z"):
            break
    else:
        break
    i+=1
    if i %1000000==0:print(step_pos)
    # print(step_pos, end="\t")

print(step_pos)
