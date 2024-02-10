from hw_2.ItemFabric import ItemFabric
from hw_2.CakeReward import CakeReward


class CakeGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук с тортом")
        return CakeReward()
