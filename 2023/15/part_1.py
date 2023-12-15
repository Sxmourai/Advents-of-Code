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

hashs = []
for line in r:
    for n in line.split(","):
        hashs.append(hash(n))

print(sum(hashs))