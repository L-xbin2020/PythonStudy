class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入")

    @classmethod
    def show_top_score(cls):
        print("历史纪律{}".format(cls.top_score))

    def start_game(self):
        print("{}开始游戏了".format(self.player_name))


# 1.查看游戏帮助信息
Game.show_top_score()
# 2.查看历史最高分
Game.show_top_score()
# 3.创建游戏对象
game = Game("lucy")
