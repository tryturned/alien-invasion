'''
Author: taobo
Date: 2020-11-12 09:03:38
LastEditTime: 2020-11-13 21:32:34
'''
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
  """单个外星人类"""
  def __init__(self, ai_setting, screen):
    super().__init__()
    self.ai_setting = ai_setting
    self.screen = screen
    self.image = pygame.image.load('images/alien.bmp')
    self.rect = self.image.get_rect()
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    self.x = self.rect.x

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def check_edges(self):
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right:
      return True
    elif self.rect.left <= 0:
      return True

  def update(self):
    self.x += self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction
    self.rect.x = self.x
    
  