import unittest
#from unittest import TestCase
#import sys
from game_classes import *
#sys.path.append('../')

class PlayerTest(unittest.TestCase):  
    def test_player_move(self):
        walls = []
        keys = []
        doors = []
        player = Player()
        player.move(30,10, walls, keys, doors) 
        #Player spawns at (80,80) so, 80 + 30 = 110 (for x) and 80 + 10 = 90 (for y)
        self.assertEqual(player.rect.x, 110)
        self.assertEqual(player.rect.y, 90)
    
    def test_player_move_single_axis(self):
        walls = []
        keys = []
        doors = []
        player = Player()
        self.assertEqual(player.rect.x, 80)
        self.assertEqual(player.rect.y, 80)
        
        #If player moves by whatever x or y, 
        #the player's new position should be the addition of its current position and the change of movement
        #If player is at (80,80), 80 + 10 = 90 (for x) and 80 + 20 = 100 (for y)
        dx = 10
        dy = 20
        player.move_single_axis(dx, dy, walls, doors, keys)
        self.assertEqual(player.rect.x, 90)
        self.assertEqual(player.rect.y, 100)

class EnemyTest(unittest.TestCase):
    def test_enemy_move_towards_player(self):
        walls =[]
        enemy = Enemy()
        player = Player()
        self.assertEqual(enemy.rect.x, 50)
        self.assertEqual(enemy.rect.y, 50)
        self.assertEqual(player.rect.x, 80)
        self.assertEqual(player.rect.y, 80)
        enemy.move_towards_player(player, 5)
        self.assertEqual(enemy.rect.x, 53)
        self.assertEqual(enemy.rect.y, 53)
        


if __name__ == 'main':
    unittest.main()