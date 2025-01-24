import pygame

class LevelSelect:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        self.font = game.font  # 使用游戏主类的字体
        
        self.levels = ["第一关", "第二关", "第三关", "返回"]
        self.current_option = 0
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.levels)
                elif event.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.levels)
                elif event.key == pygame.K_RETURN:
                    self.select_level()
                    
    def select_level(self):
        if self.current_option < 3:  # 选择关卡
            self.game.current_level = self.current_option + 1
            self.game.state = "PLAYING"
            self.game.reset_level()  # 重置游戏状态
            self.game.initialize_game_objects()  # 初始化游戏对象
        else:  # 返回
            self.game.state = "MENU"
            
    def draw(self):
        self.screen.fill((0, 105, 148))
        
        title = self.font.render("关卡选择", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_width//2, 100))
        self.screen.blit(title, title_rect)
        
        for i, level in enumerate(self.levels):
            color = (255, 255, 0) if i == self.current_option else (255, 255, 255)
            text = self.font.render(level, True, color)
            text_rect = text.get_rect(center=(self.screen_width//2, 250 + i*60))
            self.screen.blit(text, text_rect)
            
        pygame.display.flip()