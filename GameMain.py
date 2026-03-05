import pgzrun
from SpaceShooter.controller import SpaceShooter

#画面のサイズ
WIDTH = 800
HEIGHT = 600

space_shooter = SpaceShooter()

def draw():
    screen.clear()
    space_shooter.draw(screen)

def update():
    space_shooter.update(keyboard,WIDTH)

def on_key_down(key):
    space_shooter.on_key_down(key)

pgzrun.go()
