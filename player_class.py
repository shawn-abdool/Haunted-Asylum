import pygame, sys
import math
from pygame.locals import QUIT

class Player(object):
  def __init__(self):
    self.rect = pygame.Rect(1200,800,50,50)
  def move(self,dx,dy, walls, keys, doors):
    if dx!=0:
      self.move_single_axis(dx,0, walls, keys, doors)
    if dy!=0:
      self.move_single_axis(0,dy, walls, keys, doors)
  def move_single_axis(self, dx, dy, walls, keys, doors):
    self.rect.x += dx
    self.rect.y += dy
    for wall in walls:
      #Collision between player and walls
      if self.rect.colliderect(wall.rect):
        if dx > 0:
          self.rect.right = wall.rect.left
        if dx < 0:
          self.rect.left = wall.rect.right
          #self.rect.x = 0  
        if dy > 0:
          self.rect.bottom = wall.rect.top
        if dy < 0: 
          self.rect.top = wall.rect.bottom
    
    for key in keys:
      #Collision between player and keys
      if self.rect.colliderect(key.rect):
        self.keyCollided = True
        del keys[:]
        del doors[:]
            
    for door in doors:
      #Collision between player and door
      if self.rect.colliderect(door.rect):
        if dx > 0:
          self.rect.right = door.rect.left
        if dx < 0:
          self.rect.left = door.rect.right 
        if dy > 0:
          self.rect.bottom = door.rect.top
        if dy < 0: 
          self.rect.top = door.rect.bottom
        
        self.keyCollided = True
