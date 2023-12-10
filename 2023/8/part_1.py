import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input"
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

srcs = "AAA"
while src != "ZZZ":
    left,right = wasteland_map[src]
    src = right
    if steps[step_pos%(len(steps)-1)]=="L":
        src = left
    
    print(src, left, right, step_pos,steps[step_pos%(len(steps)-1)])
    step_pos+=1
print(step_pos)