from champion import *
from player import *
from database import *
from shop import *
import random
import math
from decimal import Decimal, ROUND_DOWN

class Game():
    """
    Class tổng hợp hệ thống của game bao gồm bể tướng, hiện ra tộc hệ
    """
    def __init__(self,level, exp, gold, state):
        self.state = Decimal(state)
        self.database = Database()
        self.player = Player(level, exp, gold)
        self.shop = Shop()

    """
    Cập nhật vòng khi hết vòng
    """
    def update_state(self):
        if self.state - math.floor(self.state) >= Decimal(0.8):
            self.state = self.state + Decimal(1.1) - Decimal(0.8)
        else: self.state += Decimal(0.1)

    """
    Cộng vàng dựa trên lợi tức có hoặc không có lõi
    """
    def interest_gold(self, max_interest=5):
        return min(self.gold//10, max_interest)

    """
    Cộng vàng từ chuỗi
    """
    def streak_bonus(self):
        if 4 > self.streak >=2:
            return 1
        elif self.streak ==4:
            return 2
        elif self.streak >= 5:
            return 3
        else: return 0

    """
    Cộng vàng dựa trên vòng hiện có
    """          
    def bonus_gold(self):
        self.gold += self.interest_gold()
        self.gold += self.streak_bonus()
        self.gold += 5

game = Game(level=6,exp=10,gold=200,state=Decimal(2.1))
for i in range(10):
    game.player.buy_exp()
    game.shop.shop_refresh(game.player.level)
    # print(*[obj.name if obj !=None else None for obj in  game.shop_list])
    game.player.buy_champion(game.shop, 0)
    game.player.bench_to_board(0)
    # print(*[obj.name if obj !=None else None for obj in  game.shop_list])
    # print(*[obj.name if obj !=None else None for obj in  game.list_bench])
    # if len(game.list_board)

list_name_cham = lambda list: [o.name if o != None else None for o in list]
game.shop.print_pool_size()
print(list_name_cham(game.player.list_bench))
print(list_name_cham(game.player.list_board))
