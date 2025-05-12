import menu
import pgzrun
import config
from game_manager import GameManager


WIDTH = config.WIDTH
HEIGHT = config.HEIGHT

menu = menu.Menu()
tela = "menu"
music.play("dark_forest.ogg")
game = GameManager()

def update(dt):
    global tela
    if tela == "jogo":
        game.update(dt, sounds)
        if game.game_over:
            tela = "game_over"
        

def draw():
    screen.clear()
    screen.blit("background.png", (0, 0))
    
    
    if tela == "menu":
        menu.draw_menu(screen)
    elif tela == "jogo":
        screen.clear()
        screen.blit("background.png", (0, 0))
        game.draw(screen)
    elif tela == "game_over":
        screen.clear()
        screen.blit("background.png", (0, 0))
        screen.draw.text("Game Over", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="white")
        screen.draw.text("Pressione R para reiniciar", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=30, color="white")

def on_mouse_down(pos):
    global tela, game
    if tela == "menu":
        tela = menu.handle_menu_click(pos, music)
    elif tela == "game_over":
        tela = "menu"
        game = GameManager()

def on_key_down(key):
    global tela, game
    if tela == "game_over" and key == keys.R:
        game = GameManager()
        tela = "menu"

pgzrun.go()