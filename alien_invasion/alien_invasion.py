import sys  ##sys 是 Python 的标准库模块，主要用于与 Python 解释器及其运行时环境交互。它提供了访问和维护解释器相关功能的能力
import pygame
from settings import settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()

        # self.screen = pygame.display.set_mode((1200,800))##窗口大小
        pygame.display.set_caption("Alien Invasion")
##使用存储的参数
        self.settings = settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.clock = pygame.time.Clock()##帧率控制
        #
        # self.bg_color = (230,230,230)##白色屏幕
        self.ship = Ship(self)

    def run_game(self):

        while 1:

            self.check_events()
            self.update_screen()
            self.clock.tick(60)  ##每秒60次
            # for event in pygame.event.get():
            #             #             #     if event.type == pygame.QUIT:
            #             #             #         sys.exit() #使用 sys.exit() 终止程序运行（可指定退出码）

            # self.screen.fill(self.bg_color)##屏幕颜色



            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            # pygame.display.flip()  ##调用了 pygame.display.flip()，命令 Pygame 让最近绘制的屏幕可见。这
#里，它在每次执行 while 循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新的空
#屏幕可见

            #


    def check_events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()####交互按键模块功能细化

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        # self.clock.tick(60)  ##每秒60次  时钟放这里不合适




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
###初步完成  结果是创建了一个空窗口

###哎呦！！！今天2025.6.22，太忙了，怎么办，偷个懒

###哎呦！！！今天2025.6.23，太忙了，怎么办，偷个懒


###哎呦！！！今天2025.6.24，太忙了，怎么办，偷个懒