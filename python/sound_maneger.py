class SoundManager:
    def __init__(self):
        self.music_state = True

    def toggle_music(self, music):
        self.music_state = not self.music_state
        if self.music_state:
            music.play("dark_forest.ogg")
        else:
            music.stop()

    def play_shoot(self, sound):
        if not self.music_state:
            sound.bulletsong.play()


