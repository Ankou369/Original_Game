class GameHome:
    def __init__(self):
        self.status = 1

    def draw(self):
        if status == 1:
            opening_draw()

        elif status == 2:
            menu_draw()

    def on_key_down(self,key):
        main_status = 0
        if status == 1:
            if key == keys.A:
                shooter_ship = create_shooter()
                enemy_ship = create_enemy()
                
                main_status = 2
                return main_status

            

            
                
            
            
                    
            
        
