from pgzero.builtins import keys
from .draw import menu_draw

class GameMenu:
    def draw(self,screen):
        menu_draw(screen)

    def on_key_down(self,key):
        if key == keys.A:
            main_status = 3
            return main_status

    
