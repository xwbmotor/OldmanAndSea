import pygame
import random
import os

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, is_marlin=False):
        super().__init__()
        try:
            current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            image_name = "marlin.png" if is_marlin else "fish.png"
            image_path = os.path.join(current_dir, "assets", "images", image_name)
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (40, 20))
        except:
            self.image = pygame.Surface((40, 20))
            self.image.fill((0, 191, 255) if is_marlin else (128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(2, 4)
        self.is_marlin = is_marlin
        
    def update(self):
        self.rect.x += self.speed
        if self.rect.left > 1280:
            self.rect.right = 0