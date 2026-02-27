import pgzrun
import random
import math

WIDTH =800
HEIGHT = 600

shooter_hp =10
enemy_hp =30
s_missiles = []
turn =False
eshot = 60
e_missiles =[]
status =0

shooter = Actor('shooter.png',(400,500))
enemy =Actor('eship.png',(400,100))

star = []
for i in range(30):
    rect =Rect((random.randrange(WIDTH),random.randrange(HEIGHT)),(2,2))
    star .append(rect)

#絵の描画
def draw():
    screen.clear()
    for i in range(len(star)):
        screen.draw.rect(star[i],'WHITE')
    if status ==0:

        screen.draw.text('S P A C E  S H O O T E R',(100,290),color='WHITE',gcolor = 'YELLOW',fontsize =72)
    elif status ==1:
        screen.draw.text("STAGE 1",(300,300),color ='YELLOW',fontsize =64)
        for missile in s_missiles:
            missile.draw()
        for missile in e_missiles:
            missile.draw()
        screen.draw.text('Enemy HP ='+str(enemy_hp),(50,50),color='YELLOW',fontsize =32)
        screen.draw.text('shooter HP ='+str(shooter_hp),(600,50),color='YELLOW',fontsize =32) 

    elif status == 2:
        screen.draw.text('G A M E  O V E R',(310,290),color ='WHITE',gcolor ='RED',fontsize=32)
    
    elif status == 3:
        screen.draw.text('G A M E  C L E A R',(200,290),color ='WHITE',gcolor ='YELLOW',fontsize=32)
    elif status == 4:
        screen.draw.text("STAGE 2",(110,300),color ='YELLOW',fontsize =64)
        for missile in s_missiles:
            missile.draw()
        for missile in e_missiles:
            missile.draw()
            screen.draw.text('Enemy HP ='+str(enemy_hp),(50,50),color='YELLOW',fontsize =32)
            screen.draw.text('shooter HP ='+str(shooter_hp),(600,50),color='YELLOW',fontsize =32)
    elif status == 5:
        screen.draw.text('G A M E  O V E R',(310,290),color ='WHITE',gcolor ='RED',fontsize=32)
    elif status == 6:
        screen.draw.text('G A M E  C L E A R',(200,290),color ='WHITE',gcolor ='YELLOW',fontsize=32)
    shooter.draw()
    enemy.draw()
      

def update():
    global enemy_hp,turn,eshot,shooter_hp,status
    for i in range(len(star)):
        star[i].y += i
        if star[i].y > HEIGHT:
            star[i].y =0
    if status ==1 :
        #自機のキー操作
        if keyboard.left:
            if shooter.x>47:
                shooter.x -= 3
        if keyboard.right:
            if shooter.x < WIDTH-47:
                shooter.x += 3
                
        #敵を左右に動かす
        if turn :
            enemy.x += 5
            if enemy.x > WIDTH:
                turn =False
        else:
            enemy.x -= 5
            if enemy.x <0:
                turn =True


        #敵のミサイルの角度        
        if eshot ==0:
            angle = enemy.angle_to(shooter)
            missile1 = Actor('emissile.png',(enemy.x-25,enemy.y+10))
            missile2 = Actor('emissile.png',(enemy.x+25,enemy.y+10))
            missile3 = Actor('emissile.png',(enemy.x+25,enemy.y+10))
            missile1.angle =90 +angle
            missile2.angle =90 +angle
            e_missiles.append(missile1)
            e_missiles.append(missile2)       
            eshot =60
        else:
            eshot -=1

        #敵のミサイル
        for missile in e_missiles:
            red =math.radians(-(missile.angle-90))
            missile.x += (math.cos(red)) * 3
            missile.y += (math.sin(red)) * 3
            rect =Rect(missile.topleft,(11,35))
            if shooter.colliderect(rect):
                shooter_hp -= 1
                if shooter_hp ==0:
                    status=2
                e_missiles.remove(missile)
        #自機のミサイル
        for missile in s_missiles:
            missile.y -=10
            rect =Rect(missile.topleft,(16,22))
            if enemy.colliderect(rect):
                enemy_hp -= 1
                if enemy_hp ==0:
                    status =3
                s_missiles.remove(missile)
    if status ==4:
        #自機のキー操作
        if keyboard.left:
            if shooter.x>47:
                shooter.x -= 3
        if keyboard.right:
            if shooter.x < WIDTH-47:
                shooter.x += 3
                
        #敵を左右に動かす
        if turn :
            enemy.x += 10
            if enemy.x > WIDTH:
                turn =False
        else:
            enemy.x -= 10
            if enemy.x <0:
                turn =True


        #敵のミサイルの角度        
        if eshot ==0:
            angle = enemy.angle_to(shooter)
            missile1 = Actor('emissile.png',(enemy.x-25,enemy.y+10))
            missile2 = Actor('emissile.png',(enemy.x+25,enemy.y+10))
            missile1.angle =90 +angle
            missile2.angle =90 +angle
            e_missiles.append(missile1)
            e_missiles.append(missile2)       
            eshot =30
        else:
            eshot -=1

        #敵のミサイル
        for missile in e_missiles:
            red =math.radians(-(missile.angle-90))
            missile.x += (math.cos(red)) * 3
            missile.y += (math.sin(red)) * 3
            rect =Rect(missile.topleft,(11,35))
            if shooter.colliderect(rect):
                shooter_hp -= 1
                if shooter_hp ==0:
                    status=5
                e_missiles.remove(missile)
        #自機のミサイル
        for missile in s_missiles:
            missile.y -=10
            rect =Rect(missile.topleft,(16,22))
            if enemy.colliderect(rect):
                enemy_hp -= 1
                if enemy_hp ==0:
                    status =6
                s_missiles.remove(missile)


def on_key_down(key):
    global s_missiles,e_missiles,status,enemy_hp,shooter_hp
    if key == keys.SPACE:
        #停止中
        if status == 0 or status == 2:
            enemy_hp =30
            shooter_hp=10
            s_missiles=[]
            e_missiles=[]
            status = 1
        elif status == 3:
            enemy_hp =30
            shooter_hp=10
            s_missiles=[]
            e_missiles=[]
            status =4
        #プレイ中
        elif status == 1 or status ==4 :
            s_missiles.append(Actor('smissile.png',shooter.pos))

pgzrun.go()
