import component
from vector import Vector2
class Gameobject:
    gameobject_list = []
    def __init__(self, name, transform):
        self.name = name
        self.component_list = []
        self.transform = transform
        Gameobject.gameobject_list.append(self)

    def add_componenet(self, componenet):
        self.component_list.append(componenet)

    def update(self):
        for component in self.component_list:
            component.update()

    @staticmethod
    def update_all():
        for gameobject in Gameobject.gameobject_list:
            gameobject.update()


    