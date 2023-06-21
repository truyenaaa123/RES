from champion import *
import random
from database import *

class Shop():
    """
    Class quản lý các chức năng của shop:
        - Tạo bể tướng tùy vào giá tiền dựa vào database
        - Chỉnh lại tỷ lệ khi một bể tướng hết
      * - Đổi lại tướng trong cửa hàng
    """
    def __init__(self):
        self.database = Database()
        self.pool_champion = self.create_pool_champion()
        self.shop_list = [None]*5
    
    """
    Xây dựng bể tướng
    """
    def create_pool_champion(self):
        pool_cham = {1:[],2:[],3:[],4:[],5:[]}
        for cost in self.database.list_champion.keys():
            for cham in self.database.list_champion[cost]:
                pool_cham[cost] += [cham] * self.database.pool_champion_size[cost]
        return pool_cham
    
    """
    Kiểm tra xem bể tướng còn tướng không
    Nếu có thì chỉnh lại trong số tỷ lệ về 0
    """
    def check_out_of_champion(self, level_chances):
        for idx, pool_cost in self.pool_champion.items():
            if len(pool_cost) <= 0:
                level_chances[idx-1] = 0
        return level_chances
    
    """
    Đổi lại tướng trong shop
    """
    def shop_refresh(self, level):
        for pos_shop in range(5):
            if self.shop_list[pos_shop] != None:
                self.pool_champion[self.shop_list[pos_shop].cost].append(self.shop_list[pos_shop])

        shop_list = []
        for box in range(5):
            level_chances = self.check_out_of_champion(list(self.database.rolling_chances[level].values()))
            random_value = random.choices(list(self.pool_champion.keys()),
                                          weights=level_chances,k=1)[0]
            cham = random.choice(self.pool_champion[random_value])
            self.pool_champion[random_value].remove(cham)
            shop_list.append(cham)

        self.shop_list = shop_list

    """
    In ra số lượng tướng còn lại trong bể
    """
    def print_pool_size(self):
        pool_cham_max_size = {1:377, 2:286, 3:234, 4:144, 5:80}
        print(*[str(len(self.pool_champion[cost])) + '/' + str(pool_cham_max_size[cost])  for cost in range(1,6)])

if __name__ == "__main__":
    shop = Shop()
    shop.shop_refresh(7)
    print(*[cham.name for cham in shop.shop_list])
    shop.print_pool_size()