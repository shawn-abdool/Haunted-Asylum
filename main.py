from my_imports import *
from my_levels import levels
import os
import sys
import subprocess
if __name__ == "__main__":
  import doctest
  doctest.testmod(game_classes, verbose = True)

#Initialising a timer 
starttime = time.time()

def runningGame(timeTaken):
  end_rect = pygame.Rect(0,0,0,0)
  enemy = Enemy()
  player = Player()  
  os.environ["SDL_VIDEO_CENTERED"] = "dummy"
  pygame.init()
  #Defining resolution
  pygame.display.set_caption("Haunted Asylum")

  #Taking resolution of display
  info = pygame.display.Info()
  #Storing resolution of display in variables
  screen_width, screen_height = info.current_w, info.current_h
  #Setting the window to be the resolution of the display
  screen = pygame.display.set_mode((screen_width,screen_height))
  clock = pygame.time.Clock()
  walls = []
  doors = []
  keys = []

  #creating player using class above
  colour = (0,128,255)
  
  #Store number of levels survived
  levels_survived = 0

  x = y = 0
  level = [
  "WWWWWWWWWWWWWWWWWWWWWWW",
  "W                     W",
  "W              K      W",
  "W                     W",
  "W                     W",
  "W                     W",
  "W                     W",
  "WWWWWWWWW             W",
  "W       W             W",
  "W       D             W",
  "W   E   D             W",
  "W       D             W",
  "W       W             W",
  "WWWWWWWWWWWWWWWWWWWWWWW",
  ]         
  for row in level:
    for col in row:
      if col == "W":
        Wall(x, y, walls)
      if col == "D":
        Door(x, y, doors)
      if col == "K":
        Key(x, y, keys)
      if col == "E":
        end_rect = pygame.Rect(x,y,30,30)
      x += 96
    y += 90
    x = 0

  #starting gameplay
  running = True
  while running is True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    #drawing screen
    screen.fill((0,0,0))
    for wall in walls:
      pygame.draw.rect(screen, (255,255,255),wall.rect)
    for door in doors:
      pygame.draw.rect(screen,(54,34,4),door.rect)
    for key in keys:
      pygame.draw.rect(screen,(185, 165, 61),key.rect)
    pygame.draw.rect(screen, (0,0,200),end_rect)
    pygame.draw.rect(screen,colour,player.rect)
    pygame.draw.rect(screen,(31,34,211), enemy.rect)
    pygame.display.flip() 


    #Moving enemy object
    enemy.move_towards_player(player, 2)
    enemy.move_towards_player2(player)
    #moving player
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_w]:
      player.move(0,-5, walls, keys, doors)
    if user_input[pygame.K_s]:
      player.move(0,5, walls, keys, doors)
    if user_input[pygame.K_a]:
      player.move(-5,0, walls, keys, doors)
      if player.rect.x < 0:
        player.rect.x= screen_width -1
    if user_input[pygame.K_d]:
      player.move(5,0, walls, keys, doors)
      if player.rect.x > screen_width:
        player.rect.x = -59

    if player.rect.colliderect(end_rect):
      del walls[:]
      del doors[:]
      del keys[:]
      level = random.choice(levels)
      x = y = 0
      for row in level:
        for col in row:
          if col == "W":
            Wall(x,y, walls)
          if col == "D":
            Door(x, y, doors)
          if col == "K":
            Key(x, y, keys)
          if col == "E":
            end_rect = pygame.Rect(x,y,50,50)
          x += 96
        y+= 90
        x = 0
      levels_survived += 1

    if player.rect.colliderect(enemy.rect):
      running = False
      pygame.quit()
      with open('levels_survived.txt', 'w') as f:
        f.write(str(levels_survived))
      return levels_survived

  pygame.quit()

if __name__ == '__main__':
  runningGame(starttime)
  #Taking start time and subtracting from end time
  endtime  = time.time()
  timeTaken = endtime -starttime
  #print(timeTaken)
  
  subprocess.run([sys.executable, 'death_screen.py'])

