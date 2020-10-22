import sys
import pygame

from button import Button
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats

import game_functions as gf


def run_game():
    pygame.init()
    # 初始化游戏并创建一个屏幕对象]
    ai_screen = Settings()
    screen = pygame.display.set_mode((ai_screen.screen_width,ai_screen.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    # play_button = Button(ai_screen,screen,"Play")
    play_button = Button(ai_screen,screen,"Play")

    stats = GameStats(ai_screen)
    # 创建一架飞船
    ship = Ship(ai_screen,screen)
    # 创建一个外星人
    # alien = Alien(ai_screen,screen)
    alien = Alien(ai_screen,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    # gf.create_fleet(ai_screen,screen,aliens,ship)
    # gf.create_fleet(ai_screen,screen,aliens)
    gf.create_fleet(ai_screen,screen,aliens,ship)
    # 设置背景颜色
    bg_color = (230,230,230)

    # 开始游戏的主循环
    while True:
        # 每次循环时都重绘屏幕

        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #         pass
        gf.check_events(ship,ai_screen,screen,bullets,play_button,stats)
        ship.update()
        gf.update_bullets(bullets,aliens,ai_screen,screen,ship)
        # gf.update_screen(ai_screen,screen,ship,bullets,alien)
        gf.update_screen(ai_screen,screen,ship,bullets,aliens,play_button,stats)
        gf.update_aliens(aliens,ai_screen,ship,screen,bullets,stats)


run_game()
