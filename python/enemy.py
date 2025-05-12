from pgzero.builtins import Actor
from config import WIDTH, HEIGHT, ENEMY_SPEED
import random
import math
class Enemy:
    def __init__(self, hero):
        self.images = ["alien_pink_walk1", "alien_pink_walk2"]
        self.actor = Actor(self.images[0], (0, 0))
        self.randomize_position()
        self.hero = hero
        self.enemy_speed = ENEMY_SPEED
        self.frame = 0
        self.anim_timer = 0
        self.facing = "right"

    
    def update(self, hero_pos):

        hero_x, hero_y = hero_pos

        dx = hero_x - self.actor.x
        dy = hero_y - self.actor.y

        distance = math.hypot(dx, dy)
        if distance > 0:
            dx /= distance
            dy /= distance

            self.actor.x += dx * self.enemy_speed
            self.actor.y += dy * self.enemy_speed
        
        if self.actor.x > hero_x:
            self.facing = "left"
        elif self.actor.x < hero_x:
            self.facing = "right"

        self.anim_timer += 1
        if self.anim_timer % 20 == 0:
            self.frame = (self.frame + 1) % len(self.images)
            if self.facing == "left":
                self.actor.image = self.images[self.frame] + "_left"
            else:
                self.actor.image = self.images[self.frame]
            

    def draw(self):
        self.actor.draw()

    def randomize_position(self):
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            self.actor.x = random.randint(0, WIDTH)
            self.actor.y = + 50
        elif side == "bottom":
            self.actor.x = random.randint(0, WIDTH)
            self.actor.y = HEIGHT - 50
        elif side == "left":
            self.actor.x = -50
            self.actor.y = random.randint(0, HEIGHT)
        elif side == "right":
            self.actor.x = WIDTH + 50
            self.actor.y = random.randint(0, HEIGHT)
