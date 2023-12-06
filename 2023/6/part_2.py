time = 63789468
distance = 411127420471035
ways_to_win = 0
for pressing_time in range(7274680,time):
    left_time = time-pressing_time
    speed = pressing_time
    distance_traveled = left_time*speed
    if distance_traveled>distance:
        print(pressing_time, (time-pressing_time)-pressing_time+1, distance_traveled)
        break
        ways_to_win+=1
print(ways_to_win)