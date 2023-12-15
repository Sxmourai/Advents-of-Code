import sys
FILE_NAME = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    FILE_NAME = "test_input"
with open(FILE_NAME, "r", encoding="utf-8") as f:
    r = f.read().splitlines(keepends=False)

def hash(text) -> int:
    val = 0
    for char in text:
        val += ord(char)
        val *= 17
        val = val%256
    return val

boxes = [[] for x in range(0, 256)]
for line in r:
    for n in line.split(","):
        if n[-1]=="-":
            key=n[:-1]
            for k in boxes[hash(key)]:
                if k[0]==key:
                    boxes[hash(key)].remove(k)
        else:
            key,val = n.split("=")
            index = len(boxes[hash(key)])
            for k in boxes[hash(key)]:
                if k[0]==key:
                    index = boxes[hash(key)].index(k)
                    boxes[hash(key)].remove(k)
                    break
            boxes[hash(key)].insert(index,(key,int(val)))
                
        
        # print(f"\nAfter \"{n}\":")
        # for i,box in enumerate(boxes):
        #     if box:
        #         print(f"Box {i}: {box}")

su = 0
for i,box in enumerate(boxes):
    i+=1
    for j,lens in enumerate(box):
        j+=1
        key,val = lens
        su += i*j*val
        # print(key, i,"*",j,"*",val,"=",i*j*val)
print(su)