def split_int(content, sep):
    return list(map(lambda x: int(x), filter(lambda x: x.strip() != '', content.split(sep))))
import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    time = f.readline()
    distance = f.readline()

time = split_int(time.split(":")[-1], " ")
distance = split_int(distance.split(":")[-1], " ")
s = 1
for game in range(len(time)):
    game_time = time[game]
    game_distance = distance[game]
    ways_to_win = 0
    for pressing_time in range(game_time):
        left_time = game_time-pressing_time
        speed = pressing_time
        distance_traveled = left_time*speed
        if distance_traveled>game_distance:
            ways_to_win+=1
    s *= ways_to_win
print(s)