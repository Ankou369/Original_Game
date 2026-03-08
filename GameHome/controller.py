from .draw import opening_draw,menu_draw
from pgzero.builtins import keys
class GameHome:
    def __init__(self):
        self.status = 1

    def draw(self,screen):
        if self.status == 1:
            opening_draw(screen)

        elif self.status == 2:
            menu_draw(screen)

    def on_key_down(self,key):
        main_status = 0
        if self.status == 1:
            if key == keys.SPACE:
                self.status = 2

            return None
            
        elif self.status == 2:
            if key == keys.A:
                
                main_status = 2
                return main_status

            

            
                
            
            
                    
            
        
