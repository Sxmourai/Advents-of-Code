import sys
file_name = "input"
if len(sys.argv)>1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.readlines()[:20]
nums = "0123456789"
sum_of_parts = 0
for y,line in enumerate(r):
    for symbol in line.split("."):
        if symbol.strip():
            to_remove = []
            osymbol = symbol
            for i,char in enumerate(symbol):
                if not char in nums:
                    to_remove.append(char)
            for char in to_remove:
                symbol = symbol.replace(char, "")
            try:
                x = line.index(symbol)
            except ValueError:
                print(line,symbol,osymbol)
            end = x+len(symbol)
            # print(f"{x},{y} - {r[y][x:end]}")


print(sum_of_parts)