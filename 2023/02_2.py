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
sum_ids = 0
for game_id,game in enumerate(c):
    game_id +=1 # Starts at 1
    takes = game.split(": ")[-1] # Takes second part (the cubes)

    for load in takes.split(";"):
        for take in load.split(","):
            amount,color = take.lstrip(" ").split(" ")
            amount = int(amount)
            color = color.strip() # remove potential \n
            if amount > maxs[color]:
                print(f"Game {game_id} is impossible, too much {color} ({amount} > {maxs[color]})")
                break
        else: # continue breaking if broke up ^^
            continue
        break
    else: # No break, so add id
        sum_ids += game_id
print(sum_ids) # 2256
