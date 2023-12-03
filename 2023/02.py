with open("02.input", "r") as f:
    c = f.readlines()


for game_id,game in enumerate(c):
    game_id +=1 # Starts at 1
    takes = game.split(": ")[-1] # Takes second part (the cubes)
    print("Game",game_id,":")
    for load in takes.split(";"):
        for take in load.split(","):
            amount,color = take.lstrip(" ").split(" ")
            print(f"\ttook {amount} cubes colored {color}")
