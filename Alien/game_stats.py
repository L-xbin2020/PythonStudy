class GameStats():
    """跟踪游戏信息统计"""

    def __init__(self,ai_screen):
        """初始化统计信息"""
        self.ai_screen = ai_screen
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_screen.ship_limit
