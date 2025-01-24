# old_man_and_sea/src/main.py

import pygame
from game import Game

def main():
    # 初始化pygame
    pygame.init()
    
    # 创建游戏实例
    game = Game()
    
    # 启动主循环
    game.run()

if __name__ == "__main__":
    main()