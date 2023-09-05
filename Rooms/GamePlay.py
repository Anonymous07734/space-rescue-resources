from GameFrame import Level, Globals
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Hud import Score, Lives 

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add objects
        self.add_room_object(Ship(self, 25, 50))
        self.add_room_object(Zork(self,1120, 50))
        
        # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)
        self.lives = Lives(self, Globals.SCREEN_WIDTH - 150, 20)
        self.add_room_object(self.lives)

        #add sounds
        self.bg_music = self.load_sound("Music.mp3")
        self.bg_music.set_volume(0.1)
        self.bg_music.play(loops=1)

        self.laser = self.load_sound("Laser_shot.ogg")
        self.laser.set_volume(1)

        self.ship_damage = self.load_sound("Ship_damage.ogg")
        self.ship_damage.set_volume(1)

        self.astronaut_saved = self.load_sound("Astronaut_saved.ogg")
        self.astronaut_saved.set_volume(1)

        self.astronaut_hit = self.load_sound("Astronaut_hit.ogg")
        self.astronaut_hit.set_volume(1)

        self.asteroid_shot = self.load_sound("Asteroid_shot.wav")
        self.asteroid_shot.set_volume(1)

        self.bonus_score = self.load_sound("Bonus_score.mp3")
        self.bonus_score.set_volume(0.3)

