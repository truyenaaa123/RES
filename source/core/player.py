from source.core.champion import *
from source.core.shop import *
import time
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
        self.num_bench = 9
        self.num_board = level
        self.list_cham = [None]*(9+self.num_board)
        self.is_full_cham = False
        self.database = Database()
        self.list_3stars = []

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
                self.list_cham.append(None)

    def buy_upgrade_cham(self, shop: Shop, pos_shop):
        cham = shop.shop_list[pos_shop].copy()
        list_same_cham = [idx for idx, value in enumerate(self.list_cham) if hasattr(value, 'name') and (cham.name == value.name and cham.star == value.star == 1)]
        list_same_cham_shop = [idx for idx, value in enumerate(shop.shop_list) if hasattr(value, 'name') and (cham.name == value.name and cham.star == value.star == 1)]
        if self.is_full_cham:
            # Hàng chờ full nhưng vẫn up được lên 2 sao
            if len(list_same_cham + list_same_cham_shop) >= 3 and len(list_same_cham) != 0:
                self.list_cham[list_same_cham[-1]] = None
                self.list_cham[list_same_cham[0]] = cham
                self.list_cham[list_same_cham[0]].star = 2
                self.gold -= (3-len(list_same_cham)) * shop.shop_list[pos_shop].cost
                # print("So luong tuong trên hàng chờ: ", len(list_same_cham))
                if 3-len(list_same_cham) == 1:
                    shop.shop_list[pos_shop] = None
                else:
                    shop.shop_list[pos_shop] = None
                    list_same_cham_shop.remove(pos_shop)
                    shop.shop_list[list_same_cham_shop[0]] = None
            # Hàng chờ full tướng và không up được lên 2 sao
            else:
                # print("hàng chờ đã full")
                pass
        else:
            # Mua tướng trên hàng chờ chưa full
            if len(list_same_cham) < 2:
                self.gold -= shop.shop_list[pos_shop].cost
                self.list_cham[self.list_cham.index(None)] = cham
                shop.shop_list[pos_shop] = None
            # Up tướng khi hàng chờ chưa full
            else:
                self.list_cham[list_same_cham[1]] = None
                self.gold -= shop.shop_list[pos_shop].cost
                shop.shop_list[pos_shop] = None
                self.list_cham[list_same_cham[0]].star = 2

        #up tướng lên 3 sao
        list_same_cham = [idx for idx, value in enumerate(self.list_cham) if hasattr(value, 'name') and (cham.name == value.name and value.star == 2)]
        if len(list_same_cham) == 3:  
            self.list_cham[list_same_cham[0]].star = 3
            self.list_cham[list_same_cham[1]] = None
            self.list_cham[list_same_cham[2]] = None
            self.list_3stars.append(cham.copy())
               
    """
    Chọn tướng trong shop và mua lên hàng chờ
    """
    def pick_champion(self, shop: Shop, pos_shop):
        if shop.shop_list[pos_shop] == None:
            print("Vị trí không có tướng để mua")
        elif shop.shop_list[pos_shop].cost > self.gold:
            print("Không đủ tiền để mua tướng")
        elif self.is_full_cham:
            if shop.shop_list[pos_shop].cost*2 > self.gold:
                print("Không đủ tiền để mua tướng")
            else:
                self.buy_upgrade_cham(shop, pos_shop)
        else: self.buy_upgrade_cham(shop, pos_shop)

        if self.list_cham.count(None) == 0:
            self.is_full_cham = True
        else: self.is_full_cham = False

    """
    Bán tướng trong hàng chờ tùy thuộc vào sao tướng
    """
    def sell_champion(self, shop: Shop,  pos_bench):
        if self.list_cham[pos_bench] == None:
            print("Vị trí không có tướng để bán")
        else:
            #Bán tướng 3 sao
            if self.list_cham[pos_bench].star == 3:
                for key, value in enumerate(self.list_3stars):
                    if value.name == self.list_cham[pos_bench].name:
                        self.list_3stars.remove(self.list_3stars[key])
                        break
                temp_cham = self.list_cham[pos_bench].copy()
                self.gold += temp_cham.cost * 9
                temp_cham.star = 1
                shop.pool_champion[self.list_cham[pos_bench].cost] += [cham.copy() for cham in [temp_cham]*9]
                self.list_cham[pos_bench] = None
            #Bán tướng 2 sao
            elif self.list_cham[pos_bench].star == 2:
                temp_cham = self.list_cham[pos_bench].copy()
                self.gold += temp_cham.cost * 3
                temp_cham.star = 1
                shop.pool_champion[self.list_cham[pos_bench].cost] += [cham.copy() for cham in [temp_cham]*3]
                self.list_cham[pos_bench] = None
            #Bán tướng 1 sao
            elif self.list_cham[pos_bench].star == 1:
                temp_cham = self.list_cham[pos_bench].copy()
                self.gold += temp_cham.cost
                temp_cham.star = 1
                shop.pool_champion[self.list_cham[pos_bench].cost] += [temp_cham]
                self.list_cham[pos_bench] = None
        
        # Nếu hàng chờ đầy thì gán lại giá trị False
        if self.is_full_cham:
            self.is_full_cham = False

    """
    Ấn nút roll tướng mất vàng
    """
    def roll(self, shop:Shop):
        if self.gold < 2:
            print("Không đủ tiền roll")
        else:
            shop.shop_refresh(self.level, self.list_3stars)
            self.gold -= 2

if __name__ == "__main__":
    list_name_cham = lambda list: [o.name if o != None else None for o in list]
    list_star_cham = lambda list: [o.star if o != None else None for o in list]
    player = Player(level= 6, exp=0, gold= 1000)
    shop = Shop()
    shop.shop_refresh(1, player.list_3stars)
    while True:
        print('Gold:', player.gold)
        print(*list_name_cham(player.list_cham))
        print(*list_star_cham(player.list_cham))
        print(*list_name_cham(shop.shop_list))
        print(*list_name_cham(player.list_3stars))
        shop.print_pool_size()
        select = int(input("Nhập 1 là roll, 2 là chọn vị trí mua tướng, 3 là chọn vị trí bán tướng: "))
        if select == 1:
            shop.shop_refresh(1, player.list_3stars)
            continue
        elif select == 2:
            pos_shop = int(input("Nhập vị trí tướng cần mua trong cửa hàng: "))
            player.pick_champion(shop, pos_shop)
        elif select == 3:
            pos_bench = int(input("Nhập vị trí tướng cần bán trong cửa hàng: "))
            player.sell_champion(shop, pos_bench)


    

"""    # Test mua exp
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
    print(*list_name_cham(shop.shop_list))"""
