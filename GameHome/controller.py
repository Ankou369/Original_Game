from .draw import opening_draw
from pgzero.builtins import keys

class GameHome:
    def draw(self,screen):
        opening_draw(screen)

    def on_key_down(self,key):
        if key == keys.SPACE:
            main_status = 2
            return main_status

            

            
                
            
            
                    
            
        
