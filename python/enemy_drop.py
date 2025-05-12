import random
from pgzero.actor import Actor
class EnemyDrop:
    def __init__(self, enemy):
        self.images = "energy_bullet"
        self.actor = Actor(self.images, enemy.actor.pos)
        self.exists = self.randomize_drop()
        
    def update(self):
        pass



    def draw(self, screen):
        if self.exists:
            self.actor.draw()

    def randomize_drop(self):
        return random.randint(1, 5) == 1