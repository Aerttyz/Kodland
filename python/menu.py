from pgzero.builtins import Rect
from config import *
from sound_maneger import SoundManager

sound_maneger = SoundManager()



class Menu:
    def __init__(self):
        self.buttons = []
        self.sound_state = "On"
        labels = ["Iniciar Jogo",f"Som: {self.sound_state}" ,  "Sair"]
       
        for i, label in enumerate(labels):
            x = (WIDTH - BUTTON_WIDTH) // 2
            y = HEIGHT // 2 + i * (BUTTON_HEIGHT + BUTTON_SPACING)
            rect = Rect((x, y), (BUTTON_WIDTH, BUTTON_HEIGHT))
            self.buttons.append({'label': label, 'rect': rect})

    def draw_menu(self, screen):
        screen.clear()
        screen.blit("background.png", (0, 0))
        screen.draw.text("Menu Principal", center=(WIDTH // 2, HEIGHT // 3), fontsize=50, color="white")
        for button in self.buttons:
            rect = button['rect']
            label = button['label']
            screen.draw.filled_rect(rect, (0, 0, 0))
            screen.draw.text(label, center = rect.center, fontsize=30, color=(255, 255, 255))

    def handle_menu_click(self, pos, music):
        for button in self.buttons:
            if button['rect'].collidepoint(pos):
                if button['label'] == "Iniciar Jogo":
                    return "jogo"
                elif button['label'] == f"Som: {self.sound_state}":
                    sound_maneger.toggle_music(music)
                    self.sound_state = "Off" if self.sound_state == "On" else "On"
                    button['label'] = f"Som: {self.sound_state}"
                elif button['label'] == "Sair":
                    exit()
        return "menu"
