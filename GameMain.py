import pgzrun
from Core.GameManager import GameManager
from GameHome.controller import GameHome
from GameMenu.controller import GameMenu
from SpaceShooter.controller import SpaceShooter


#画面のサイズ
WIDTH = 800
HEIGHT = 600

status = 1

game_home = GameHome()
game_menu = GameMenu()
space_shooter = SpaceShooter()
game_manager = GameManager()


def draw():
    screen.clear()
    if status == 1:
        game_home.draw(screen)

    elif status == 2:
        game_menu.draw(screen)
        

    elif status == 3:
        space_shooter.draw(screen)

def update():
    global status
    if status == 3:
        space_shooter.update(keyboard,WIDTH)

def on_key_down(key):
    global status
    if status == 1:
        result = game_home.on_key_down(key)
        if result is not None:
            status = result

    elif status == 2:
        result = game_menu.on_key_down(key)
        if result is not None:
            status = result
        if status == 3:
            space_shooter.reset()
            
        

    elif status == 3:
        space_shooter.on_key_down(key)
        result = game_manager.on_key_down(key)
        if result is not None:
            status = result


    
        
    

    
pgzrun.go()
