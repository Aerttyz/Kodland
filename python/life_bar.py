from config import HERO_HEALTH, WIDTH
class LifeBar:
    def __init__(self):
        self.total_hearts = HERO_HEALTH
        self.current_health = HERO_HEALTH
        self.images = ["suit_hearts", "suit_hearts_broken"]
        self.heart_spacing = 50

    def lose_life(self):
        if self.current_health > 0:
            self.current_health -= 1
    
    def gain_life(self):
        if self.current_health < self.total_hearts:
            self.current_health += 1
    
    def draw(self, screen):
        start_x = 10
        y = 10
        for i in range(self.total_hearts):
            img = self.images[0] if i < self.current_health else self.images[1]
            screen.blit(img, (start_x + i * self.heart_spacing, y))