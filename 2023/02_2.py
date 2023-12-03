import sys
file_name = "02"
if len(sys.argv)>1 and sys.argv[1] == "test":
    file_name += "_test"
with open(f"{file_name}.input", "r") as f:
    c = f.readlines()

maxs = {
    "red": 12,
    "green": 13,
    "blue": 14
}
sum_powers = 0
for game_id,game in enumerate(c):
    game_id +=1 # Starts at 1
    takes = game.split(": ")[-1] # Takes second part (the cubes)
    mins = {
        "red":  0,
        "green":0,
        "blue": 0,
    }
    for load in takes.split(";"):
        for take in load.split(","):
            amount,color = take.lstrip(" ").split(" ")
            amount = int(amount)
            color = color.strip() # remove potential \n
            
            if amount > mins[color]:
                mins[color] = amount
    print(f"Min for game {game_id} is {mins}")
    sum_powers += mins["red"] * mins["green"] * mins["blue"]
print(sum_powers)
