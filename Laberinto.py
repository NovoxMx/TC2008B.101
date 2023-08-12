import sys
import random
import pygame

class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(96, 96, 32, 32)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
       
        self.rect.x += dx
        self.rect.y += dy

       
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: 
                    self.rect.right = wall.rect.left
                if dx < 0: 
                    self.rect.left = wall.rect.right
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                if dy < 0: 
                    self.rect.top = wall.rect.bottom


class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0]+64, pos[1]+64, 32, 32)

pygame.init()
screen = pygame.display.set_mode((760, 600))

clock = pygame.time.Clock()
walls = [] 
player = Player() 


level1 = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X                  X",
    "X         XXXXXX   X",
    "X   XXXX       X   X",
    "X   X        XXXX  X",
    "X XXX  XXXX        X",
    "X   X     X X      X",
    "X   X     X   XXX XX",
    "X   XXX XXX   X X  X",
    "X     X   X   X X  X",
    "XXX   X   XXXXX X  X",
    "X X      XX        X",
    "X X   XXXX   XXX   X",
    "X     X    E   X   X",
    "XXXXXXXXXXXXXXXXXXXX",
]

level2 = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X                  X",
    "X         XXXXXX   X",
    "X   XXXX       X   X",
    "X   X        XXXX  X",
    "X XXX              X",
    "X   X     X X     EX",
    "X   X         XXX XX",
    "X   XXX       X X  X",
    "X     X       X X  X",
    "XXX   X         X  X",
    "X X                X",
    "X X   XXXX   XXX   X",
    "X     X        X   X",
    "XXXXXXXXXXXXXXXXXXXX",
]

level3 = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X    X  X  X       X",
    "X         XXXXXX   X",
    "X   XXXX       X   X",
    "X   X        XXXX  X",
    "X XXX  XXXX        X",
    "X   X     X X      X",
    "X   X     X   XXX XX",
    "X   XXX XXX   X X  X",
    "X     X   X   X X  X",
    "XXX   X   XXXXX X  X",
    "X X      XX        X",
    "X X   XXXX   XXX   X",
    "X          E   X   X",
    "XXXXXXXXXXXXXXXXXXXX",
]

list = ['level1', 'level2', 'level3']

random.choice(list)

x = y = 0

if random.choice(list) == 'level1':
    for row in level1:
        for col in row:
            if col == "X":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x+64, y+64, 32, 32)
            x += 32
        y += 32
        x = 0
elif random.choice(list) == 'level2':
    for row in level2:
        for col in row:
            if col == "X":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x+64, y+64, 32, 32)
            x += 32
        y += 32
        x = 0       
else:
    for row in level3:
        for col in row:
            if col == "X":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x+64, y+64, 32, 32)
            x += 32
        y += 32
        x = 0

running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)


    if player.rect.colliderect(end_rect):
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    
    pygame.display.flip()
    clock.tick(360)

pygame.quit()   