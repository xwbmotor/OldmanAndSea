import pygame

class Settings:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        self.font = game.font
        
        # 设置选项和状态
        self.settings = {
            "volume": 100,  # 音量 0-100
            "difficulty": 0,  # 难度 0-简单 1-普通 2-困难
            "weather": True,  # 天气效果开关
        }
        
        self.difficulty_names = ["简单", "普通", "困难"]
        self.options = ["音量", "难度", "天气效果", "返回"]
        self.current_option = 0
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.current_option == 3:  # 返回
                        self.game.state = "MENU"
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.change_setting()
                    
    def change_setting(self):
        keys = pygame.key.get_pressed()
        
        if self.current_option == 0:  # 音量调节
            if keys[pygame.K_LEFT]:
                self.settings["volume"] = max(0, self.settings["volume"] - 10)
            elif keys[pygame.K_RIGHT]:
                self.settings["volume"] = min(100, self.settings["volume"] + 10)
                
        elif self.current_option == 1:  # 难度调节
            if keys[pygame.K_LEFT]:
                self.settings["difficulty"] = (self.settings["difficulty"] - 1) % 3
            elif keys[pygame.K_RIGHT]:
                self.settings["difficulty"] = (self.settings["difficulty"] + 1) % 3
                
        elif self.current_option == 2:  # 天气效果开关
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                self.settings["weather"] = not self.settings["weather"]
        
        # 应用设置到游戏
        self.apply_settings()
        
    def apply_settings(self):
        # 设置音量
        pygame.mixer.music.set_volume(self.settings["volume"] / 100)
        
        # 设置难度（影响鲨鱼数量和速度）
        self.game.difficulty = self.settings["difficulty"]
        
        # 设置天气效果
        self.game.weather.enabled = self.settings["weather"]
        
    def draw(self):
        self.screen.fill((0, 105, 148))
        
        title = self.font.render("游戏设置", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_width//2, 100))
        self.screen.blit(title, title_rect)
        
        # 显示设置选项
        settings_text = [
            f"音量: {self.settings['volume']}%",
            f"难度: {self.difficulty_names[self.settings['difficulty']]}",
            f"天气效果: {'开' if self.settings['weather'] else '关'}",
            "返回"
        ]
        
        for i, text in enumerate(settings_text):
            color = (255, 255, 0) if i == self.current_option else (255, 255, 255)
            text_surface = self.font.render(text, True, color)
            text_rect = text_surface.get_rect(center=(self.screen_width//2, 250 + i*60))
            self.screen.blit(text_surface, text_rect)
            
        # 显示操作提示
        hint_text = "使用↑↓选择选项，←→调整数值"
        hint_surface = self.font.render(hint_text, True, (200, 200, 200))
        hint_rect = hint_surface.get_rect(center=(self.screen_width//2, 600))
        self.screen.blit(hint_surface, hint_rect)
        
        pygame.display.flip()