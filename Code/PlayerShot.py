from Code.Const import ENTITY_SPEED
from Code.Entity import Entity


class Playershot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]