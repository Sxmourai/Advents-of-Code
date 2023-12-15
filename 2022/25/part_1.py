import sys
file_name = "input"
if len(sys.argv)>1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.read()

def snafu_int(digit):
    return "=-012".index(digit)-2

def int_snafu(digit):
    if digit == "0":return "0"
    if digit == "1":return "1"
    if digit == "2":return "2"
    if digit == "3":return "1="
    if digit == "4":return "1-"
    if digit == "5":return "10"
    if digit == "6":return "11"
    if digit == "7":return "12"
    if digit == "8":return "13"
    if digit == "9":return "2="

def int_to_snafu(n):
    if n/5>5:
        cs=n%5
    digits = list(reversed(n))
    32-25=7
    100+7=32
    7-5=2
    7=12
    112
    32
    cs = "0"
    for i,digit in enumerate(digits):
        pos = 10**i
        idigit = int_snafu(digit)
        if len(idigit)==2:
            cs+=(10**(i+1))*int(idigit[0])
            cs+=(10**(i+1))*int(idigit[0])
        cs += pos*idigit
    return cs
    

s = 0
for line in r.splitlines(keepends=False):
    digits = list(reversed(line))
    cs = 0
    for i,digit in enumerate(digits):
        pos = 5**i
        idigit = snafu_int(digit)
        cs += pos*idigit
    s+=cs

print(s, "->", int_to_snafu(s))