import zope.interface
from hw_2.IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class CakeReward:
    def open(self):
        print("Открыли сундук с тортом")
