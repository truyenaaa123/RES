from champion import *
import random
import math
from decimal import Decimal, ROUND_DOWN

class Game():
    """
    Class tổng hợp hệ thống của game bao gồm bể tướng, hiện ra tộc hệ
    """
    def __init__(self,level, exp, gold, state):
        self.level = level
        self.exp = exp
        self.gold = gold
        self.streak = 0
        self.level_max = 9
        self.list_bench = [None]*9
        self.list_board = [None]*level
        self.state = Decimal(state)
        self.list_champion = self.create_champion_by_cost()
        self.rolling_chances = self.create_rolling_chances()
        self.pool_champion_size = self.create_pool_size()
        self.pool_champion = self.create_pool_champion()
        self.shop_list = [None]*5
        self.exp_size = self.create_exp_size()       
    
    """
    Tạo danh sách các tướng theo giá tiền kèm tộc hệ
    """
    def create_champion_by_cost(self):
        list_cham = {1:[], 2:[], 3:[], 4:[], 5:[]}

        list_cham[1].append(Champion("Cassiopeia", {"Noxus":True,"Shurima":True,"Invoker":True}, 1))
        list_cham[1].append(Champion("Chogath", {"Void":True, "Bruiser":True}, 1))
        list_cham[1].append(Champion("Irelia", {"Ionia":True, "Challenger":True}, 1))
        list_cham[1].append(Champion("Jhin", {"Ionia":True, "Deadeye":True}, 1))
        list_cham[1].append(Champion("Kayle", {"Demacia":True, "Slayer":True}, 1))
        list_cham[1].append(Champion("Malzahar", {"Void":True, "Sorcerer":True}, 1))
        list_cham[1].append(Champion("Maokai", {"Shadow Isles":True, "Bastion":True}, 1))
        list_cham[1].append(Champion("Orianna", {"Piltover":True, "Sorcerer":True}, 1))
        list_cham[1].append(Champion("Poppy", {"Demacia":True, "Bastion":True, "Yordle":True}, 1))
        list_cham[1].append(Champion("Renekton", {"Shurima":True, "Bruiser":True}, 1))
        list_cham[1].append(Champion("Samira", {"Noxus":True, "Challenger":True}, 1))
        list_cham[1].append(Champion("Tristana", {"Yordle":True, "Gunner":True}, 1))
        list_cham[1].append(Champion("Viego", {"Shadow Isles":True, "Rogue":True}, 1))

        list_cham[2].append(Champion("Ashe", {"Freljord":True, "Deadeye":True}, 2))
        list_cham[2].append(Champion("Galio", {"Demacia":True, "Invoker":True}, 2))
        list_cham[2].append(Champion("Jinx", {"Zaun":True, "Gunner":True}, 2))
        list_cham[2].append(Champion("Kassadin", {"Void":True, "Bastion":True}, 2))
        list_cham[2].append(Champion("Kled", {"Noxus":True, "Yordle":True, "Slayer":True}, 2))
        list_cham[2].append(Champion("Sett", {"Ionia":True, "Juggernaut":True}, 2))
        list_cham[2].append(Champion("Soraka", {"Targon":True, "Invoker":True}, 2))
        list_cham[2].append(Champion("Swain", {"Noxus":True, "Sorcerer":True, "Strategist":True}, 2))
        list_cham[2].append(Champion("Taliyah", {"Shurima":True, "Multicaster":True}, 2))
        list_cham[2].append(Champion("Teemo", {"Strategist":True, "Multicaster":True, "Yordle":True}, 2))
        list_cham[2].append(Champion("Vi", {"Piltover":True, "Bruiser":True}, 2))
        list_cham[2].append(Champion("Warwick", {"Zaun":True, "Challenger":True, "Juggernaut":True}, 2))
        list_cham[2].append(Champion("Zed", {"Ionia":True, "Rogue":True, "Slayer":True}, 2))

        list_cham[3].append(Champion("Akshan", {"Shurima":True, "Deadeye":True}, 3))
        list_cham[3].append(Champion("Darius", {"Noxus":True, "Juggernaut":True}, 3))
        list_cham[3].append(Champion("Ekko", {"Zaun":True, "Piltover":True, "Rogue":True}, 3))
        list_cham[3].append(Champion("Garen", {"Demacia":True, "Juggernaut":True}, 3))
        list_cham[3].append(Champion("Jayce", {"Piltover":True, "Gunner":True}, 3))
        list_cham[3].append(Champion("Kalista", {"Shadow Isles":True, "Challenger":True}, 3))
        list_cham[3].append(Champion("Karma", {"Ionia":True, "Invoker":True}, 3))
        list_cham[3].append(Champion("Katarina", {"Noxus":True, "Rogue":True}, 3))
        list_cham[3].append(Champion("Lissandra", {"Freljord":True, "Invoker":True}, 3))
        list_cham[3].append(Champion("RekSai", {"Void":True, "Bruiser":True}, 3))
        list_cham[3].append(Champion("Sona", {"Demacia":True, "Multicaster":True}, 3))
        list_cham[3].append(Champion("Taric", {"Targon":True, "Sorcerer":True, "Bastion":True}, 3))
        list_cham[3].append(Champion("Velkoz", {"Void":True, "Multicaster":True, "Sorcerer":True}, 3))

        list_cham[4].append(Champion("Aphelios", {"Targon":True, "Deadeye":True}, 4))
        list_cham[4].append(Champion("Azir", {"Shurima":True, "Strategist":True}, 4))
        list_cham[4].append(Champion("Gwen", {"Shadow Isles":True, "Slayer":True}, 4))
        list_cham[4].append(Champion("Jarvan IV", {"Demacia":True, "Strategist":True}, 4))
        list_cham[4].append(Champion("Kaisa", {"Void":True, "Challenger":True}, 4))
        list_cham[4].append(Champion("Lux", {"Demacia":True, "Sorcerer":True}, 4))
        list_cham[4].append(Champion("Nasus", {"Shurima":True, "Juggernaut":True}, 4))
        list_cham[4].append(Champion("Sejuani", {"Freljord":True, "Bruiser":True}, 4))
        list_cham[4].append(Champion("Shen", {"Ionia":True, "Bastion":True, "Invoker":True}, 4))
        list_cham[4].append(Champion("Urgot", {"Zaun":True, "Deadeye":True}, 4))
        list_cham[4].append(Champion("Yasuo", {"Ionia":True, "Challenger":True}, 4))
        list_cham[4].append(Champion("Zeri", {"Zaun":True, "Gunner":True}, 4))

        list_cham[5].append(Champion("Aatrox", {"Darkin":True, "Juggernaut":True, "Slayer":True}, 5))
        list_cham[5].append(Champion("Ahri", {"Ionia":True, "Sorcerer":True}, 5))
        list_cham[5].append(Champion("Belveth", {"Void":True, "Empress":True}, 5))
        list_cham[5].append(Champion("Heimerdinger", {"Piltover":True, "Technogenius":True, "Yordle":True}, 5))
        list_cham[5].append(Champion("KSante", {"Shurima":True, "Bastion":True}, 5))
        list_cham[5].append(Champion("Ryze", {"Wanderer":True, "Invoker":True}, 5))
        list_cham[5].append(Champion("Senna", {"Shadow Isles":True, "Redeemer":True, "Gunner":True}, 5))
        list_cham[5].append(Champion("Sion", {"Noxus":True, "Bruiser":True}, 5))

        return list_cham

    """
    Tạo tỷ lệ roll cho từng cấp độ
    """
    def create_rolling_chances(self):
        rolling_chances = {1:{1:1,2:0,3:0,4:0,5:0},
                           2:{1:1,2:0,3:0,4:0,5:0},
                           3:{1:75,2:25,3:0,4:0,5:0},
                           4:{1:55,2:30,3:15,4:0,5:0},
                           5:{1:45,2:33,3:20,4:2,5:0},
                           6:{1:25,2:40,3:30,4:5,5:0},
                           7:{1:19,2:30,3:35,4:15,5:1},
                           8:{1:16,2:20,3:35,4:25,5:4},
                           9:{1:9,2:15,3:30,4:30,5:16},
                           10:{1:5,2:10,3:20,4:40,5:25},
                           11:{1:1,2:2,3:12,4:50,5:35},
                           }
        return rolling_chances

    """
    Xây dựng bể tướng
    """
    def create_pool_champion(self):
        pool_cham = {1:[],2:[],3:[],4:[],5:[]}
        for cost in self.list_champion.keys():
            for cham in self.list_champion[cost]:
                pool_cham[cost] += [cham] * self.pool_champion_size[cost]
        return pool_cham

    """
    Tạo giá trị tối đa cho số tướng có thể xuất hiện
    """
    def create_pool_size(self):
        return {1:29,2:22,3:18,4:12,5:10}

    """
    Tạo số lượng exp cần có để lên cấp
    """
    def create_exp_size(self):
        return {3:6, 4:10, 5:24, 6:40, 7:60, 8:84, 9:10}

    """
    In ra tộc hệ gồm có tướng gì
    """
    def print_champion_by_traits(self):
        traits = []
        for cost in self.list_champion.keys():
            for chaim in self.list_champion[cost]:
                for trait in chaim.traits.keys():
                    if trait not in traits:
                        print(trait, end=": ")
                        traits.append(trait)
                        for cost_2 in self.list_champion.keys():
                            for chaim_2 in self.list_champion[cost_2]:
                                for trait_2 in chaim_2.traits.keys():
                                    if trait_2 == trait:
                                        print(chaim_2.name, end=" ")
                        print() 

    """
    In ra bảng tỷ lệ theo cấp
    """
    def print_rolling_chances(self):
        for level in self.rolling_chances.keys():
            pro = self.rolling_chances[level]
            print(str(level) + ": ", end="")
            print(*[str(temp) for temp in pro.values()])

    """
    In ra số lượng tướng còn lại trong bể
    """
    def print_pool_size(self):
        print(*[len(self.pool_champion[cost]) for cost in range(1,6)])

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
    def shop_refresh(self):
        for pos_shop in range(5):
            if self.shop_list[pos_shop] != None:
                self.pool_champion[self.shop_list[pos_shop].cost].append(self.shop_list[pos_shop])

        shop_list = []
        for box in range(5):
            level_chances = self.check_out_of_champion(list(self.rolling_chances[self.level].values()))
            random_value = random.choices(list(self.pool_champion.keys()),
                                          weights=level_chances,k=1)[0]
            cham = random.choice(self.pool_champion[random_value])
            self.pool_champion[random_value].remove(cham)
            shop_list.append(cham)

        self.shop_list = shop_list

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

    """
    Mua kinh nghiệm bằng tiền
    """
    def buy_exp(self):
        if self.gold <= 4:
            print("Hết tiền không mua được EXP")
        elif self.level == self.level_max:
            print("Level tối đa không nâng cấp được")
        else:
            self.exp += 4
            self.gold -= 4
            if self.exp >= self.exp_size[self.level]:
                self.exp -= self.exp_size[self.level]
                self.level += 1
                self.list_board.append(None)
            
    """
    Mua tướng trong shop lên hàng chờ
    """
    def buy_champion(self, pos_shop):
        if self.list_bench.count(None) == 0:
            print("hàng chờ đã full")
        else:
            for pos in range(9):
                if self.list_bench[pos] == None:
                    self.list_bench[pos] = self.shop_list[pos_shop]
                    self.shop_list[pos_shop] = None
                    break

    """
    Bán tướng trong hàng chờ
    """
    def sell_champion_bench(self, pos_bench):
        if self.list_bench.count(None) == 9:
            print("Hàng chờ không có tướng")
        elif self.list_bench[pos_bench] == None:
            print("Vị trí không có tướng để bán")
        else:
            self.pool_champion[self.list_bench[pos_bench][1]].append(self.list_bench[pos_bench][0])
            self.list_bench[pos_bench] = None

    """
    Bán tướng trên sàn
    """
    def sell_champion_board(self, pos_board):
        if self.list_board.count(None) == 9:
            print("Hàng chờ không có tướng")
        elif self.list_board[pos_board] == None:
            print("Vị trí không có tướng để bán")
        else:
            self.pool_champion[self.list_board[pos_board][1]].append(self.list_board[pos_board][0])
            self.list_board[pos_board] = None

    """
    Chuyển từ hàng chờ sang sàn đấu
    """
    def bench_to_board(self, pos_bech):
        if self.list_board.count(None) == 0:
            print("Sàn đấu đã dầy")
        else:
            for pos in range(len(self.list_board)):
                if self.list_board[pos] == None:
                    self.list_board[pos] = self.list_bench[pos_bech]
                    self.list_bench[pos_bech] = None
                    break

    """
    Ấn nút roll tướng mất vàng
    """
    def roll(self):
        if self.gold < 2:
            print("Không đủ tiền roll")
        else:
            self.shop_refresh()
            self.gold -= 2


game = Game(level=6,exp=10,gold=200,state=Decimal(2.1))
for i in range(200):
    game.buy_exp()
    game.shop_refresh()
    # print(*[obj.name if obj !=None else None for obj in  game.shop_list])
    game.buy_champion(0)
    game.bench_to_board(0)
    # print(*[obj.name if obj !=None else None for obj in  game.shop_list])
    # print(*[obj.name if obj !=None else None for obj in  game.list_bench])
    # if len(game.list_board)

game.print_pool_size()