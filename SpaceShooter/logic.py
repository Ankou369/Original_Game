from pgzero.actor import Actor
from pygame import Rect
import math

#自機のキー操作
def move_shooter(shooter, keyboard, WIDTH):
    if keyboard.left:
        if shooter.actor.x>47:
            shooter.actor.x -= 3
    if keyboard.right:
        if shooter.actor.x < WIDTH-47:
            shooter.actor.x += 3

def enemy_missile_angle(enemy,shooter):
    angle = enemy.actor.angle_to(shooter.actor)
    missile1 = Actor('emissile.png',(enemy.actor.x-25,enemy.actor.y+10))
    missile2 = Actor('emissile.png',(enemy.actor.x+25,enemy.actor.y+10))
    missile1.angle =90 +angle
    missile2.angle =90 +angle
    enemy.missiles.append(missile1)
    enemy.missiles.append(missile2)

#敵を左右に動かす
def move_enemy(status,enemy,turn,WIDTH):
    width_adjust = 80
    
    if turn:
        enemy.actor.x += 5 * ((status + 1) // 3) # 2ならSTAGE１,5ならSTAGE2
        if enemy.actor.x + width_adjust > WIDTH:
            turn = False
    else:
        enemy.actor.x -= 5 * ((status + 1)// 3) # 2ならSTAGE１,5ならSTAGE2
        if enemy.actor.x - width_adjust < 0:
            turn = True

    return turn

#敵のミサイル
def enemy_missile(status,enemy, shooter):
    now_stage = (status + 1) // 3
    for missile in enemy.missiles:
        red =math.radians(-(missile.angle-90))
        missile.x += (math.cos(red)) * 3
        missile.y += (math.sin(red)) * 3
        rect =Rect(missile.topleft,(11,35))
        if shooter.actor.colliderect(rect):
            shooter.hp -= 1
            if shooter.hp ==0:
                status= 1 + (3 * now_stage)
            enemy.missiles.remove(missile)
    return status,shooter

#自機のミサイル
def shooter_missile(status,enemy, shooter):
    now_stage = (status + 1) // 3
    for missile in shooter.missiles:
        missile.y -=10
        rect =Rect(missile.topleft,(16,22))
        if enemy.actor.colliderect(rect):
            enemy.hp -= 1
            if enemy.hp ==0:
                status = (3 * now_stage)
            shooter.missiles.remove(missile)
    return status,enemy
