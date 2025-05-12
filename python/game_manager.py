from enemy import Enemy
from hero import Hero
from config import WIDTH, HEIGHT, ENEMY_SPAWN_INTERVAL, ENEMY_SPAWN_TIMER, HERO_HEALTH
from enemy_drop import EnemyDrop
from life_bar import LifeBar

class GameManager:
    def __init__(self):
        self.hero = Hero((WIDTH // 2, HEIGHT // 2))
        self.enemies = []
        self.spawn_timer = ENEMY_SPAWN_TIMER
        self.spawn_interval = ENEMY_SPAWN_INTERVAL
        self.drops = []
        self.hero_health = HERO_HEALTH
        self.lifebar = LifeBar()
        self.game_over = False
    
    def update(self, dt, sound):
        self.hero.update(sound)
        self.collision()
        self.check_game_over()
        for enemy in self.enemies:
            enemy.update(self.hero.actor.pos)
        
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_enemy()
            self.spawn_timer = 0

    def draw(self, screen):
        self.hero.draw(screen)
        for enemy in self.enemies:
            enemy.draw()
        for drop in self.drops:
            drop.draw(screen)
        self.lifebar.draw(screen)

    def spawn_enemy(self):
        enemy = Enemy(self.hero)
        enemy.randomize_position()
        self.enemies.append(enemy)

    def collision(self):
        for enemy in self.enemies:
            if self.hero.actor.colliderect(enemy.actor):
                self.enemies.remove(enemy)
                if self.hero_health >= 0:
                    self.hero_health -= 1
                    self.lifebar.lose_life()
                break
        for projectile in self.hero.projectiles:
            for enemy in self.enemies:
                if projectile.colliderect(enemy.actor):
                    self.enemies.remove(enemy)
                    self.hero.projectiles.remove(projectile)
                    drop = EnemyDrop(enemy)
                    if drop.exists:
                        self.drops.append(drop)
                    break
        for drop in self.drops:
            if self.hero.actor.colliderect(drop.actor):
                self.drops.remove(drop)
                self.hero.hero_bullets += 10
                break
    
    def reset_game(self):
        self.enemies.clear()
        self.drops.clear()
        self.hero_health = HERO_HEALTH
        self.lifebar.current_health = HERO_HEALTH
        self.spawn_timer = 0
        self.game_over = False
    
    def check_game_over(self):
        global tela
        if self.lifebar.current_health <= 0:
            self.game_over = True
            tela = "game_over"