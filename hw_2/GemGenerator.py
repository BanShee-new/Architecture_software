from hw_2.ItemFabric import ItemFabric
from hw_2.GemReward import GemReward


class GemGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (изумруд)")
        return GemReward()