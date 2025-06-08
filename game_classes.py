import pygame, sys
import math

class Enemy(object):
  def __init__(self):
    self.rect = pygame.Rect(200,200,60,60)
  def move_towards_player(self, player, speed):
    self.speed = speed
    # Find direction vector (dx, dy) between enemy and player.
    dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
    dist = math.hypot(dx, dy)
    if dist != 0:
      dx, dy = dx / dist, dy / dist  # Normalise.
    # Move along this normalised vector towards the player at current speed.
    self.rect.x += dx * self.speed
    self.rect.y += dy * self.speed 
  
  def move_towards_player2(self, player):
    # Find direction vector (dx, dy) between enemy and player.
    dirvect = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
    if dirvect.length_squared() > 0:
      dirvect = dirvect.normalize()
    # Move along this normalised vector towards the player at current speed.
    if dirvect.length_squared() > 0:
      dirvect.scale_to_length(self.speed) 
    self.rect.move_ip(dirvect)
    
#Defining object, walls
class Wall(object):
  def __init__(self, wx, wy, walls):
    walls.append(self)
    self.rect = pygame.Rect(wx, wy, 96, 90) #Size of walls

class Door(object):
  def __init__(self, wx, wy, doors):
    doors.append(self)
    self.rect = pygame.Rect(wx, wy, 96, 90)

class Key(object):
  def __init__(self, wx, wy, keys):
    keys.append(self)
    self.rect = pygame.Rect(wx, wy, 30, 30)