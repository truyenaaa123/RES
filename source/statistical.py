from champion import *
from shop import *
from player import *
import random
import math
from decimal import Decimal, ROUND_DOWN
list_name_cham = lambda list: [o.name if o != None else None for o in list]
list_star_cham = lambda list: [o.star if o != None else None for o in list]
class Statistical(Player):
    """
    Class tổng hợp hệ thống của game bao gồm bể tướng, hiện ra tộc hệ
    """
    def __init__(self,level):
        super().__init__(level,0,1000)
        self.list_cham = [None] * (9 + self.level)
        self.sort_cham_dict = {}

    # Add vào dict để quản lý strategy
    def buy_add_to_cham_dict(self, shop:Shop, cham:Champion, total_pick):
        if cham.name not in self.sort_cham_dict:
            self.sort_cham_dict[cham.name] = total_pick
        else: 
            self.sort_cham_dict[cham.name] += total_pick    

    # Strategy mua tướng ở cost cụ thể ngẩu nhiên lên 2,3 sao
    def any4gold2star(self, shop:Shop):
        for cham_idx, cham in enumerate(shop.shop_list):
            if cham!= None and cham.cost == 1:
                num_none_shop = shop.shop_list.count(None)
                # Kiểm tra xem tướng 3 sao để không mua thêm nữa
                if cham.name in self.sort_cham_dict and self.sort_cham_dict[cham.name] == 9:
                    pass
                else: 
                    self.pick_champion(shop, cham_idx)

                    # Mua mà không cần bán (hàn chờ còn trống)
                    if num_none_shop < shop.shop_list.count(None):
                        self.buy_add_to_cham_dict(shop, cham, shop.shop_list.count(None) - num_none_shop)

                    # Cần bán để mua (hàng chờ full)
                    elif cham.name in self.sort_cham_dict:
                        # Số lượng nhỏ nhất trên sàn của một cham
                        min_num_cham = list(self.sort_cham_dict.items())[-1]

                        # Kiểm tra xem đây có phải là cham duy nhất mà nhỏ nhất
                        if cham.name == min_num_cham[0] and list(self.sort_cham_dict.values()).count(min_num_cham[1]) == 1:
                            pass
                        else:
                            # Cham cần bán
                            sell_cham = list(self.sort_cham_dict.keys())[-1]
                            if sell_cham == cham.name:
                                sell_cham = list(self.sort_cham_dict.keys())[-2]

                            # Kiểm tra xem nên bán tướng cần bán như thế nào (Chỉ bán 1 sao hay bán cả 2 sao)
                            if min_num_cham[1] == 1 or min_num_cham[1] == 2 or min_num_cham[1] == 3 or min_num_cham[1] == 6:
                                for pos_bench, cham_bench in enumerate(self.list_cham):
                                    if cham_bench.name == sell_cham:
                                        self.sell_champion(shop, pos_bench)
                                        self.pick_champion(shop, cham_idx)
                                        self.buy_add_to_cham_dict(shop,cham, 1)
                                        break
                            elif min_num_cham[1] == 4 or min_num_cham[1] == 5 or min_num_cham[1] == 7:
                                for pos_bench, cham_bench in enumerate(self.list_cham):
                                    if cham_bench.name == sell_cham and cham_bench.star == 1:
                                        self.sell_champion(shop, pos_bench)
                                        self.pick_champion(shop, cham_idx)
                                        self.buy_add_to_cham_dict(shop,cham, 1)
                                        break
                            # Bán xong thì cần trừ ngược vào danh sách hoặc xóa khỏi danh sách khi sl về 0
                            if min_num_cham[1]%3 == 0:
                                self.sort_cham_dict[sell_cham] -=3
                            else: self.sort_cham_dict[sell_cham] -= 1
                            if self.sort_cham_dict[sell_cham] == 0:
                                del self.sort_cham_dict[sell_cham]

                    sort_cham_list = sorted(self.sort_cham_dict.items(), key=lambda x: x[1], reverse=True)
                    self.sort_cham_dict = dict(sort_cham_list)

            if list_star_cham(self.list_cham).count(2) + list_star_cham(self.list_cham).count(3) == 5:
                # print(*list_star_cham(self.list_cham))
                # for cham in self.list_cham:
                #     if cham != None and cham.star == 2:
                #         print(cham.name)
                return False
            # self.printUI(shop)
        return True

    def printUI(self, shop:Shop):
        print(self.is_full_cham)
        print("Hàng chờ")
        print(*list_name_cham(self.list_cham))
        print(*list_star_cham(self.list_cham))
        print()
        print("Cửa hàng")
        print(*list_name_cham(shop.shop_list))
        print()
        print(self.sort_cham_dict)

            
if __name__ == "__main__":

    total = 0
    loop = 10000
    gold = 0

    for i in range(loop):
        shop = Shop()
        statistical = Statistical(4)
        shop.shop_refresh(statistical.level, statistical.list_3stars)
        count = 0
        while(statistical.any4gold2star(shop)):
            count += 1
            shop.shop_refresh(statistical.level, statistical.list_3stars)
            # print(*list_name_cham(shop.shop_list))
        gold += (1000- statistical.gold)
        total += count

    print(total/loop)
    print(gold/loop)

        