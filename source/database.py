from champion import *
import random
import math
from decimal import Decimal, ROUND_DOWN


class Database():
    """
    Class tổng hợp các thông số trong game bao gồm:
        - Danh sách tướng và tộc hệ
        - Tỷ lệ roll cho từng cấp
        - Số lượng tướng tối đa có thể roll ra được
        - Số exp cần thiết để lên level
    """
    def __init__(self):
        self.list_champion = self.create_champion_by_cost()
        self.rolling_chances = self.create_rolling_chances()
        self.pool_champion_size = self.create_pool_size()
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
        rolling_chances = {1:{1:100,2:0,3:0,4:0,5:0},
                           2:{1:100,2:0,3:0,4:0,5:0},
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
    In ra bảng tỷ lệ theo cấp
    """
    def print_rolling_chances(self):
        for level in self.rolling_chances.keys():
            pro = self.rolling_chances[level]
            print(str(level) + ": ", end="")
            print(*[str(temp) for temp in pro.values()])
    
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
    
if __name__ == "__main__":
    data = Database()
    data.print_rolling_chances()
    data.print_champion_by_traits()