from pgzero.builtins import keys
class GameManager:
    def on_key_down(self,key):
        if key == keys.P:
            main_status = 2
            return main_status
    
