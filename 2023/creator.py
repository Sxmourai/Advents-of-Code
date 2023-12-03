import os,sys,requests
if len(sys.argv)>1:
    day = sys.argv[1]
else:print("Please input a day")
try:
    os.mkdir(day)
except FileExistsError:print("Directory already exists, is day already created ?")
sessionToken = os.getenv('AoC_token')
if sessionToken==None:
    print("Please set AoC_token to your token in your env variables")
    aoc_input = ""
else:
    print("Getting input...")
    aoc_input = requests.get(f"https://adventofcode.com/2023/day/{day}/input", headers={'Cookie': 'session='+sessionToken}).content.decode()

with open(f"{day}/input", "w") as f:
    f.write(aoc_input)

# Test input
from bs4 import BeautifulSoup
tr = requests.get(f"https://adventofcode.com/2023/day/{day}", headers={'Cookie': 'session='+sessionToken})
soup = BeautifulSoup(tr.content.decode(), 'html.parser')
test_input = list(soup.find("pre").children)[0].text
with open(f"{day}/test_input", "w") as f:
    f.write(test_input)

with open(f"{day}/part_1.py", "a") as f:
    f.write("")
os.system(f"code {day}/part_1.py")
with open(f"{day}/part_2.py", "a") as f:
    f.write("")