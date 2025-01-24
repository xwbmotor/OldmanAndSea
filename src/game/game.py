import pygame
import sys
import random
import os
from scenes.menu import Menu
from scenes.level_select import LevelSelect
from scenes.settings import Settings
from models.fisherman import Fisherman
from models.fish import Fish
from models.shark import Shark  # 添加此行
from utils.weather import Weather

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("老人与海")
        
        # 统一字体设置
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        font_path = os.path.join(current_dir, "assets", "fonts", "chinese.ttf")
        
        try:
            self.font = pygame.font.Font(font_path, 36)
        except FileNotFoundError:
            print(f"无法加载字体文件: {font_path}")
            print("尝试加载系统字体...")
            try:
                self.font = pygame.font.SysFont("microsoftyaheui", 36)
            except:
                print("加载系统字体失败，使用默认字体")
                self.font = pygame.font.Font(None, 36)
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_level = 1
        self.difficulty = 0  # 默认简单难度
        
        # 初始化场景，传递字体对象
        self.state = "MENU"
        self.menu = Menu(self)
        self.level_select = LevelSelect(self)
        self.settings = Settings(self)
        
        # 创建游戏对象
        self.all_sprites = pygame.sprite.Group()
        self.fishes = pygame.sprite.Group()
        self.sharks = pygame.sprite.Group()
        
        self.fisherman = Fisherman(600, 360)
        self.all_sprites.add(self.fisherman)
        
        # 添加鱼群
        for _ in range(5):
            fish = Fish(random.randint(0, 1280), random.randint(100, 620))
            self.all_sprites.add(fish)
            self.fishes.add(fish)
            
        # 添加马林鱼
        self.marlin = Fish(random.randint(0, 1280), random.randint(100, 620), True)
        self.all_sprites.add(self.marlin)
        self.fishes.add(self.marlin)
        
        # 天气系统
        self.weather = Weather(self.screen)
        
        # 添加分数系统
        self.score = 0
        self.fish_spawn_timer = 0
        self.shark_spawn_timer = 0
        
        # 创建鲨鱼组
        self.sharks = pygame.sprite.Group()
        
        # 生成初始鲨鱼
        for _ in range(3):
            shark = Shark(random.randint(0, 1280), random.randint(100, 620))
            self.all_sprites.add(shark)
            self.sharks.add(shark)
        
        # 倒计时设置
        self.countdown = 180  # 3分钟 = 180秒
        self.start_time = None
        self.target_score = 200
        
        # 天气系统初始化
        self.weather.change_weather()  # 随机初始天气
        self.weather_change_timer = 0
        
        self.initialize_game_objects()
        
    def initialize_game_objects(self):
        # 创建精灵组
        self.all_sprites = pygame.sprite.Group()
        self.fishes = pygame.sprite.Group()
        self.sharks = pygame.sprite.Group()
        
        # 创建渔夫
        self.fisherman = Fisherman(600, 360)
        self.all_sprites.add(self.fisherman)
        
        # 添加鱼群
        for _ in range(5):
            fish = Fish(random.randint(0, 1280), random.randint(100, 620))
            self.all_sprites.add(fish)
            self.fishes.add(fish)
            
        # 添加马林鱼
        self.marlin = Fish(random.randint(0, 1280), random.randint(100, 620), True)
        self.all_sprites.add(self.marlin)
        self.fishes.add(self.marlin)
        
        # 根据难度调整鲨鱼数量和速度
        shark_count = {0: 2, 1: 3, 2: 4}[self.difficulty]
        shark_speed = {0: 2, 1: 3, 2: 4}[self.difficulty]
        
        for _ in range(shark_count):
            shark = Shark(random.randint(0, 1280), random.randint(100, 620))
            shark.speed = shark_speed
            self.all_sprites.add(shark)
            self.sharks.add(shark)
        
    def run(self):
        while self.running:
            if self.state == "MENU":
                self.menu.handle_input()
                self.menu.draw()
            elif self.state == "LEVEL_SELECT":
                self.level_select.handle_input()
                self.level_select.draw()
            elif self.state == "SETTINGS":
                self.settings.handle_input()
                self.settings.draw()
            elif self.state == "PLAYING":
                self.handle_game_events()
                self.update_game()
                self.render_game()
                
            self.clock.tick(60)
            
    def start_new_game(self):
        self.current_level = 1
        self.state = "PLAYING"
        
    def show_level_select(self):
        self.state = "LEVEL_SELECT"
        
    def show_settings(self):
        self.state = "SETTINGS"
        
    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = "MENU"
                    
    def update_game(self):
        self.all_sprites.update()
        self.weather.update()
        
        # 更新计时器
        self.fish_spawn_timer += 1
        self.shark_spawn_timer += 1
        
        # 每5秒生成新的小鱼
        if self.fish_spawn_timer >= 300:
            fish = Fish(0, random.randint(100, 620))
            self.all_sprites.add(fish)
            self.fishes.add(fish)
            self.fish_spawn_timer = 0
            
        # 每10秒生成新的鲨鱼
        if self.shark_spawn_timer >= 600:
            shark = Shark(0, random.randint(100, 620))
            self.all_sprites.add(shark)
            self.sharks.add(shark)
            self.shark_spawn_timer = 0
            
        # 鲨鱼追踪马林鱼
        for shark in self.sharks:
            shark.target = self.marlin
            
        # 检测鲨鱼捕食马林鱼
        shark_hits = pygame.sprite.spritecollide(self.marlin, self.sharks, False)
        if shark_hits:
            self.marlin.kill()
            self.score -= 50
            self.marlin = Fish(random.randint(0, 1280), random.randint(100, 620), True)
            self.all_sprites.add(self.marlin)
            self.fishes.add(self.marlin)
            
        # 检测渔夫捕鱼
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            hits = pygame.sprite.spritecollide(self.fisherman, self.fishes, True)
            for fish in hits:
                if fish.is_marlin:
                    self.score += 100
                    print("捕获马林鱼! +100分")
                else:
                    self.score += 10
                    print("捕获小鱼! +10分")
        
        # 更新倒计时
        if self.start_time is None:
            self.start_time = pygame.time.get_ticks()
        
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        self.countdown = max(180 - elapsed_time, 0)
        
        # 更新天气
        self.weather_change_timer += 1
        if self.weather_change_timer >= 1800:  # 每30秒改变一次天气
            self.weather.change_weather()
            self.weather_change_timer = 0
            
        # 检查游戏结束条件
        if self.countdown <= 0:
            if self.score >= self.target_score:
                print(f"恭喜通过第{self.current_level}关!")
                self.current_level += 1
                if self.current_level > 3:
                    self.state = "MENU"
                else:
                    self.reset_level()
            else:
                print("时间到！任务失败")
                self.state = "MENU"
                
    def render_game(self):
        self.screen.fill((0, 105, 148))  # 海蓝色背景
        
        # 绘制波浪
        for y in range(0, 720, 20):
            pygame.draw.line(self.screen, (0, 155, 198), 
                           (0, y), (1280, y + 10))
        
        # 绘制精灵
        self.all_sprites.draw(self.screen)
        
        # 绘制天气效果
        self.weather.draw()
        
        # 显示当前关卡
        level_text = self.font.render(f"第{self.current_level}关", True, (255, 255, 255))
        self.screen.blit(level_text, (10, 10))
        
        # 显示分数
        score_text = self.font.render(f"分数: {self.score}/{self.target_score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 50))
        
        # 显示倒计时
        minutes = self.countdown // 60
        seconds = self.countdown % 60
        time_text = self.font.render(f"时间: {minutes:02d}:{seconds:02d}", True, (255, 255, 255))
        self.screen.blit(time_text, (10, 90))
        
        # 显示天气状态
        weather_text = self.font.render(f"天气: {self.weather.get_weather_name()}", True, (255, 255, 255))
        self.screen.blit(weather_text, (10, 130))
        
        pygame.display.flip()
        
    def reset_level(self):
        self.score = 0
        self.countdown = 180
        self.start_time = None
        self.weather.change_weather()
        self.fish_spawn_timer = 0
        self.shark_spawn_timer = 0
        self.target_score = 200 * self.current_level  # 根据关卡调整目标分数