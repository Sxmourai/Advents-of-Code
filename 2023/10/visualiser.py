import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.read()

map = r.splitlines(keepends=False)
for y,row in enumerate(map):
    for x,char in enumerate(row):
        if char == "S":
            start_x,start_y = x,y
import pygame
pygame.init()
sw,sh = 800,600
screen = pygame.display.set_mode([sw,sh])
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()
running = True
w = sw/len(map[0])
h = sh/len(map)
while running:
    clock.tick(60)
    screen.fill((255,255,255))
    for py,row in enumerate(map):
        for px,char in enumerate(row):
            x = px*w
            y = py*h
            # pygame.draw.rect(screen, (0,255,0), ((x+1,y+1), (w-1, h-1)))
            if char == "|":
                x += w/2
                pygame.draw.line(screen, (255,0,0),(x,y), (x,y+h), 1)
            elif char == "-":
                y = y+h/2
                pygame.draw.line(screen, (255,0,0),(x,y), (x+w,y), 1)
            elif char == "L":
                x = x+w/2
                pygame.draw.line(screen, (255,0,0),(x,y), (x,y+h/2), 1)
                pygame.draw.line(screen, (255,0,0),(x,y+h/2), (x+w/2,y+h/2), 1)
            elif char == "J":
                x = x+w/2
                pygame.draw.line(screen, (255,0,0),(x,y), (x,y+h/2), 1)
                pygame.draw.line(screen, (255,0,0),(x,y+h/2), (x-w/2,y+h/2), 1)
            elif char == "7":
                y = y+h/2
                pygame.draw.line(screen, (255,0,0),(x,y), (x+w/2,y), 1)
                pygame.draw.line(screen, (255,0,0),(x+w/2,y), (x+w/2,y+h/2), 1)
            elif char == "F":
                x = x+w
                y = y+h/2
                pygame.draw.line(screen, (255,0,0),(x,y), (x-w/2,y), 1)
                pygame.draw.line(screen, (255,0,0),(x-w/2,y), (x-w/2,y+h/2), 1)
            # else:
            #     print(char)
            #     pas
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    pygame.display.update()

pygame.quit()

# neighbors = [
#     (-1, 0),(0,-1),(0,1),(1,0)
# ]
# def follow_loop():

# for nx,ny in neighbors:
#     x = nx+start_x
#     y = ny+start_y
#     char = map[y][x]
#     if ny != 0 and char in "F|7":
#         follow_loop()
#     if nx != 0 and char in "L-J":
#         follow_loop()