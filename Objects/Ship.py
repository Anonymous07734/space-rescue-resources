from GameFrame import Globals, RoomObject
from Objects.Laser import Laser
import pygame

walking = True

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True

        self.can_shoot = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down, left and right
        """
        
        if key[pygame.K_w]:
            self.y -= 10
        elif key[pygame.K_s]:
            self.y += 10
        elif key[pygame.K_a]:
            self.x -= 10
        elif key[pygame.K_d]:
            self.x += 10
        if key[pygame.K_SPACE]:
            self.shoot_laser()
        elif key[pygame.K_l]:
            self.shooting_laser()
        if key[pygame.K_p]:
            self.room.score.update_score(+99)
            self.room.bonus_score.play()
    
            
    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
        elif self.x < 0:
            self.x = 0
        elif self.x + self.height> Globals.SCREEN_HEIGHT:
            self.x = Globals.SCREEN_HEIGHT - self.height

    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room() 

    def shoot_laser(self):
        """
        Shoots a laser from the ship
        """
        if self.can_shoot:
            new_laser = Laser(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            self.room.laser.play()
        
       
    def shooting_laser(self):
       if walking == True:
            new_lasers = Laser(self.room, self.x + self.width, self.y + self.height/2 - 4)
            self.room.add_room_object(new_lasers)
            self.room.laser.play()
     

    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True