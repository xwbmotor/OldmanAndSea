# menu.py

import pygame
import sys
import os

class Menu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        
        # 修改字体路径
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        font_path = os.path.join(current_dir, "assets", "fonts", "chinese.ttf")
        
        try:
            self.font = pygame.font.Font(font_path, 36)
        except FileNotFoundError:
            # 如果找不到自定义字体，使用系统默认字体
            self.font = pygame.font.SysFont("microsoftyaheui", 36)
        
        # 菜单选项
        self.options = ["开始新游戏", "关卡选择", "游戏设置", "退出游戏"]
        self.current_option = 0
        
        # 按钮颜色
        self.normal_color = (255, 255, 255)
        self.selected_color = (255, 255, 0)
        
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
                    self.select_option()
                    
    def select_option(self):
        if self.options[self.current_option] == "开始新游戏":
            self.game.start_new_game()
        elif self.options[self.current_option] == "关卡选择":
            self.game.show_level_select()
        elif self.options[self.current_option] == "游戏设置":
            self.game.show_settings()
        elif self.options[self.current_option] == "退出游戏":
            pygame.quit()
            sys.exit()
            
    def draw(self):
        self.screen.fill((0, 105, 148))  # 海蓝色背景
        
        # 绘制标题
        title = self.font.render("老人与海", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_width//2, 100))
        self.screen.blit(title, title_rect)
        
        # 绘制菜单选项
        for i, option in enumerate(self.options):
            color = self.selected_color if i == self.current_option else self.normal_color
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.screen_width//2, 250 + i*60))
            self.screen.blit(text, text_rect)
            
        pygame.display.flip()