import pgzrun
from SpaceShooter.controller import SpaceShooter
from GameHome.controller import GameHome

#画面のサイズ
WIDTH = 800
HEIGHT = 600

status = 1

game_home = GameHome()
space_shooter = SpaceShooter()


def draw():
    screen.clear()
    if status == 1:
        game_home.draw(screen)

    elif status == 2:
        space_shooter.draw(screen)

def update():
    global status
    if status == 2:
        space_shooter.update(keyboard,WIDTH)

def on_key_down(key):
    global status
    if status == 1:
        result = game_home.on_key_down(key)

        if result is not None:
            status = result
            
    if status == 2:
        space_shooter.on_key_down(key)

    
pgzrun.go()
