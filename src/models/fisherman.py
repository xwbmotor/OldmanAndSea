import pygame
import os

class Fisherman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            image_path = os.path.join(current_dir, "assets", "images", "fisherman.png")
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 60))  # 渔夫和小船
        except:
            self.image = pygame.Surface((50, 50))
            self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.caught_fish = None
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def operation(self):
        # 操作船只的方法
        pass

    def attack(self):
        # 攻击鲨鱼的方法
        pass

    def catch(self):
        # 捕捉马林鱼的方法
        pass

    def find(self):
        # 寻找马林鱼的方法
        pass