#!/usr/bin/python
# coding:utf-8
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 10
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 30
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 2
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Scoring
        self.alien_points = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 2

        # fleet_direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



