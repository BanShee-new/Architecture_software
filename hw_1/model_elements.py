from ModelElements.polygonal_model import PolygonalModel
from ModelElements.flash import Flash
from ModelElements.camera import Camera
from ModelElements.scene import Scene
from .IModelChanger import IModelChanger
from .IModelChangedObserver import IModelChangedObserver


class ModelStore(IModelChanger):
    def __init__(self, changedObserver: IModelChangedObserver):
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []
        self.__changedObserver = changedObserver

        self.models.append(PolygonalModel)
        self.flashes.append(Flash())
        self.cameras.append(Camera())
        self.scenes.append(Scene(0, self.models, self.flashes, self.cameras))

    def get_scene(self, id: int):
        for i in range(len(self.scenes)):
            if self.scenes[i].id == id:
                return self.scenes[i]
        return None

    def notify_change(self, sender):
        pass
