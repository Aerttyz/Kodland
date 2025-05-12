import pgzrun
from pgzero.actor import Actor
from pgzero.builtins import keyboard, images
from pgzero.screen import Screen
from config import SHOOTING_COOLDOWN, BULLET_SPEED, HERO_BULLETS, WIDTH
from sound_maneger import SoundManager

class Hero:
    def __init__(self, pos):
        self.idle_image = ["character_robot_hold", "character_robot_idle", "character_robot_behind_back"]
        self.images = ["character_robot_run0","character_robot_run1", "character_robot_run2"]
        self.hero_shooting = ["character_robot_attack0", "character_robot_attack1", "character_robot_attack2"]
        self.actor = Actor(self.idle_image[0], pos)
        self.frame = 0
        self.facing = "right"
        self.anim_timer = 0
        self.moving = False
        self.projectiles = []
        self.shooting_cooldown = SHOOTING_COOLDOWN
        self.bullet_speed = BULLET_SPEED
        self.sound_manager = SoundManager()
        self.hero_bullets = HERO_BULLETS

        

        self.direction = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0),
            'left_up': (-1, -1),
            'left_down': (-1, 1),
            'right_up': (1, -1),
            'right_down': (1, 1)
        }

    def update(self, sounds):
        dx = dy = 0
        self.moving = False
        if keyboard.right and keyboard.up:
            self.facing = 'right_up'
            dx, dy = 2.5, -2.5
        elif keyboard.right and keyboard.down:
            self.facing = 'right_down'
            dx, dy = 2.5, 2.5
        elif keyboard.left and keyboard.up:
            self.facing = 'left_up'
            dx, dy = -2.5, -2.5
        elif keyboard.left and keyboard.down:
            self.facing = 'left_down'
            dx, dy = -2.5, 2.5
        elif keyboard.right:
            self.facing = 'right'
            dx = 2.5
        elif keyboard.left:
            self.facing = 'left'
            dx = -2.5
        elif keyboard.up:
            self.facing = 'up'
            dy = -2.5
        elif keyboard.down:
            self.facing = 'down'
            dy = 2.5

        next_pos_x = self.actor.x + dx
        next_pos_y = self.actor.y + dy

        if 0 < next_pos_x < 800 and 0 < next_pos_y < 500:
            if dx != 0 or dy != 0:
                self.moving = True
                self.actor.x += dx
                self.actor.y += dy

        if self.moving:
            self.anim_timer += 1
            if self.anim_timer % 5 == 0:
                self.frame = (self.frame + 1) % len(self.images)
                if self.facing == 'left' or self.facing == 'left_up' or self.facing == 'left_down':
                    self.actor.image = self.images[self.frame] + "_left"
                else:
                    self.actor.image = self.images[self.frame]
        else:
            self.anim_timer += 1
            if self.anim_timer % 50 == 0:
                self.frame = (self.frame + 1) % len(self.idle_image)
                self.actor.image = self.idle_image[self.frame]
        
        if self.shooting_cooldown > 0:
            self.shooting_cooldown -= 1 / 60

        if keyboard.space:
            if self.shooting_cooldown <= 0 and self.hero_bullets > 0:  
                self.shoot()
                self.sound_manager.play_shoot(sounds)
                self.shooting_cooldown = SHOOTING_COOLDOWN
                self.hero_bullets -= 1
    

            

    def draw(self, screen: Screen):
        if self.facing == 'left':
            img = getattr(images, self.actor.image)
            x = self.actor.x - img.get_width() // 2
            y = self.actor.y - img.get_height() // 2
            screen.blit(self.actor.image, (x, y))
        else:
            self.actor.draw()
        
        for bullet in self.projectiles:
                bullet.x += bullet.vx
                bullet.y += bullet.vy
                bullet.draw()
                
                if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 500:
                    self.projectiles.remove(bullet)
        screen.draw.text(
        f'Bullet: {self.hero_bullets}', topright=(WIDTH - 10, 40), color='white', fontsize=24)
        
    
    def shoot(self):
        bullet = Actor("character_robot_bullet", (self.actor.x, self.actor.y))

        bullet.vx, bullet.vy = self.direction.get(self.facing, (0, 0))
        bullet.vx *= self.bullet_speed
        bullet.vy *= self.bullet_speed
        self.projectiles.append(bullet)
    