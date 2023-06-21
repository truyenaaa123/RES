from champion import *
from shop import *
import random
import math
from decimal import Decimal, ROUND_DOWN

class Player():
    """
    Class tổng hợp hệ thống của game bao gồm bể tướng, hiện ra tộc hệ
    """
    def __init__(self,level, exp, gold):
        self.level = level
        self.exp = exp
        self.gold = gold
        self.streak = 0
        self.level_max = 9
        self.list_bench = [None]*9
        self.list_board = [None]*level
        self.database = Database()

    """
    Mua kinh nghiệm bằng tiền
    """
    def buy_exp(self):
        if self.gold < 4:
            print("Hết tiền không mua được EXP")
        elif self.level == self.level_max:
            print("Level tối đa không nâng cấp được")
        else:
            self.exp += 4
            self.gold -= 4
            if self.exp >= self.database.exp_size[self.level]:
                self.exp -= self.database.exp_size[self.level]
                self.level += 1
                self.list_board.append(None)
            
    """
    Mua tướng trong shop lên hàng chờ
    """
    def buy_champion(self, shop: Shop, pos_shop):
        if self.list_bench.count(None) == 0:
            print("hàng chờ đã full")
        elif shop.shop_list[pos_shop] == None:
            print("Vị trí không có tướng để mua")
        else:
            for pos in range(9):
                if self.list_bench[pos] == None:
                    if shop.shop_list[pos_shop].cost <= self.gold:
                        self.list_bench[pos] = shop.shop_list[pos_shop]
                        self.gold -= shop.shop_list[pos_shop].cost
                        shop.shop_list[pos_shop] = None
                        break
                    else:
                        print("Không đủ tiền để mua tướng")
                        break

    """
    Bán tướng trong hàng chờ
    """
    def sell_champion_bench(self, shop: Shop,  pos_bench):
        if self.list_bench.count(None) == 9:
            print("Hàng chờ không có tướng")
        elif self.list_bench[pos_bench] == None:
            print("Vị trí không có tướng để bán")
        else:
            shop.pool_champion[self.list_bench[pos_bench].cost].append(self.list_bench[pos_bench])
            self.list_bench[pos_bench] = None

    """
    Bán tướng trên sàn
    """
    def sell_champion_board(self, shop: Shop, pos_board):
        if self.list_board.count(None) == 9:
            print("Hàng chờ không có tướng")
        elif self.list_board[pos_board] == None:
            print("Vị trí không có tướng để bán")
        else:
            shop.pool_champion[self.list_board[pos_board].cost].append(self.list_board[pos_board])
            self.list_board[pos_board] = None

    """
    Chuyển từ hàng chờ sang sàn đấu
    """
    def bench_to_board(self, pos_bech):
        if self.list_board.count(None) == 0:
            print("Sàn đấu đã dầy")
        elif self.list_bench[pos_bech] == None:
            print("Không có tướng tại vị trí hàng chờ này")
        else:
            for pos in range(len(self.list_board)):
                if self.list_board[pos] == None:
                    self.list_board[pos] = self.list_bench[pos_bech]
                    self.list_bench[pos_bech] = None
                    break

    """
    Ấn nút roll tướng mất vàng
    """
    def roll(self, shop:Shop):
        if self.gold < 2:
            print("Không đủ tiền roll")
        else:
            shop.shop_refresh(self.level)
            self.gold -= 2

if __name__ == "__main__":
    list_name_cham = lambda list: [o.name if o != None else None for o in list]
    player = Player(level= 6, exp=0, gold= 100)
    shop = Shop()
    shop.shop_refresh(player.level)
    # Test mua exp
    player.buy_exp()
    print('exp: ', player.exp)
    print('gold: ', player.gold)
    print()

    # Test mua tướng
    player.buy_champion(shop, pos_shop=0)
    player.buy_champion(shop, pos_shop=0)
    player.buy_champion(shop, pos_shop=1)
    shop.print_pool_size()
    print('gold: ', player.gold)
    print(*list_name_cham(player.list_bench))
    print()

    # Test chuyển từ hàng chờ sang sàn đấu
    player.bench_to_board(0)
    player.bench_to_board(0)
    print(*list_name_cham(player.list_bench))
    print(*list_name_cham(player.list_board))
    print()

    # Test bán tướng trên hàng chờ và sàn đấu
    player.sell_champion_bench(shop, 0)
    player.sell_champion_bench(shop, 1)
    player.sell_champion_board(shop, 0)
    player.sell_champion_board(shop, 1)
    print(*list_name_cham(player.list_bench))
    print(*list_name_cham(player.list_board))
    shop.print_pool_size()
    print(*list_name_cham(shop.shop_list))
