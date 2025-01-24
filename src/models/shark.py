import pygame
import math
import os

class Shark(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            image_path = os.path.join(current_dir, "assets", "images", "shark.png")
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (60, 30))
        except:
            self.image = pygame.Surface((60, 30))
            self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.target = None
    
    def update(self):
        if self.target:
            dx = self.target.rect.centerx - self.rect.centerx
            dy = self.target.rect.centery - self.rect.centery
            dist = math.sqrt(dx * dx + dy * dy)
            
            if dist != 0:
                dx = dx / dist * self.speed
                dy = dy / dist * self.speed
                self.rect.x += dx
                self.rect.y += dy