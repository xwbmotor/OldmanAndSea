import pygame
import random

class Weather:
    def __init__(self, screen):
        self.screen = screen
        self.weather_type = "sunny"  # sunny, cloudy, rainy
        self.rain_drops = []
        self.weather_names = {
            "sunny": "晴天",
            "cloudy": "阴天",
            "rainy": "雨天"
        }
        
    def change_weather(self):
        self.weather_type = random.choice(["sunny", "cloudy", "rainy"])
        
    def update(self):
        if self.weather_type == "rainy":
            if random.random() < 0.3:
                self.rain_drops.append([random.randint(0, 1280), 0])
            for drop in self.rain_drops[:]:
                drop[1] += 5
                if drop[1] > 720:
                    self.rain_drops.remove(drop)
                    
    def draw(self):
        if self.weather_type == "cloudy":
            pygame.draw.circle(self.screen, (200, 200, 200), (100, 100), 30)
        elif self.weather_type == "rainy":
            for drop in self.rain_drops:
                pygame.draw.line(self.screen, (200, 200, 255), 
                               (drop[0], drop[1]), (drop[0], drop[1]+5), 2)
                               
    def get_weather_name(self):
        return self.weather_names[self.weather_type]