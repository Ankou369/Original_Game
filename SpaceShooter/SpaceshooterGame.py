import pgzrun
from dataclass import dataclass

#画面のサイズ
WIDTH = 800
HEIGHT = 600

status = 1

#SPACE SHOOTER　宣言
@dataclass
class enemy_record:
    actor: object
    hp: int
    missiles:list

def create_shooter():
    return enemy_record(
    actor=Actor('shooter.png',(400,500)),
    hp=10,
    missiles=[]
)
shooter_ship = create_shooter()

def create_enemy():
    return enemy_record(
    actor=Actor('eship.png',(400,100)),
    hp=1,
    missiles=[]
)
enemy_ship = create_enemy()

ship_table = [shooter_ship, enemy_ship]

turn =False
eshot = 60

#####　SPACE SHOOTER(DRAW)　#######################################################################
def space_shooter_draw(status,enemy_ship,shooter_ship):
    #SPACE SHOOTER オープニング
    if status == 3:
        screen.draw.text('S P A C E  S H O O T E R',(120,290),color='WHITE',gcolor = 'YELLOW',fontsize =72)
        game_start_guide()

        shooter_ship.actor.draw()
        enemy_ship.actor.draw()

    else:
        battle_draw(status,enemy_ship, shooter_ship)
    

                
def battle_draw(status,enemy_ship, shooter_ship):
    #SPACE SHOOTER HPの描写
    hp = [(f'Enemy HP = {enemy_ship.hp}'    ,(50 ,50)),
          (f'Shooter HP = {shooter_ship.hp}',(600,50))]
    
    now_stage = (status-1) // 3 # 4,5ならSTAGE１,７,8ならSTAGE2
    #SPACE SHOOTER STAGE1
    if status ==4 or status == 7:
        screen.draw.text(f'STAGE {now_stage}',(300,300),color ='YELLOW',fontsize =64)

        #ミサイルの描写
        for missile in shooter_ship.missiles:
            missile.draw()
        for missile in enemy_ship.missiles:
            missile.draw()
        #HPの描写
        for text,pos in hp:
            screen.draw.text(text,pos,color='YELLOW',fontsize = 32)

        shooter_ship.actor.draw()
        enemy_ship.actor.draw()
    elif status == 5 or status ==8:
        screen.draw.text('G A M E  C L E A R',(310,290),color ='WHITE',gcolor ='YELLOW',fontsize=32)
        shooter_ship.actor.draw()
        
        if now_stage == 1:
            game_middle_guide()
        else:
            game_end_guide()
            

    elif status == 6 or status == 9:
        screen.draw.text('G A M E  O V E R',(310,290),color ='WHITE',gcolor ='RED',fontsize=32)
        enemy_ship.actor.draw()
        
        game_over_guide()
        


    
    
    
    
    
#####　SPACE SHOOTER(UPDATE)　#####################################################################
def space_shooter_update(status,enemy_ship, shooter_ship,eshot):
    #自機のキー操作
    move_shooter(shooter_ship)
    
    #敵を左右に動かす
    move_enemy(status,enemy_ship)       


    #敵のミサイルの角度        
    if eshot ==0:
        enemy_missile_angle(enemy_ship,shooter_ship)
        eshot = 60 #時間をリセット 
    else:
        eshot -=1
        

    #敵のミサイル
    status,shooter_ship = enemy_missile(status,enemy_ship, shooter_ship)
        

    #自機のミサイル
    status,enemy_ship = shooter_missile(status,enemy_ship, shooter_ship)

    return status,enemy_ship,shooter_ship,eshot


#自機のキー操作
def move_shooter(shooter_ship):
    if keyboard.left:
        if shooter_ship.actor.x>47:
            shooter_ship.actor.x -= 3
    if keyboard.right:
        if shooter_ship.actor.x < WIDTH-47:
            shooter_ship.actor.x += 3

def enemy_missile_angle(enemy_ship,shooter_ship):
    angle = enemy_ship.actor.angle_to(shooter_ship.actor)
    missile1 = Actor('emissile.png',(enemy_ship.actor.x-25,enemy_ship.actor.y+10))
    missile2 = Actor('emissile.png',(enemy_ship.actor.x+25,enemy_ship.actor.y+10))
    missile1.angle =90 +angle
    missile2.angle =90 +angle
    enemy_ship.missiles.append(missile1)
    enemy_ship.missiles.append(missile2)

#敵を左右に動かす
def move_enemy(status,enemy_ship):
    global turn
    width_adjust = 80
    
    if turn :
        enemy_ship.actor.x += 5 * (status // 3) # 4ならSTAGE１,７ならSTAGE2
        if enemy_ship.actor.x + width_adjust > WIDTH:
            turn = False
    else:
        enemy_ship.actor.x -= 5 * (status // 3) # 4ならSTAGE１,７ならSTAGE2
        if enemy_ship.actor.x - width_adjust < 0:
            turn = True
#敵のミサイル
def enemy_missile(status,enemy_ship, shooter_ship):
    now_stage = (status - 1) // 3
    for missile in enemy_ship.missiles:
        red =math.radians(-(missile.angle-90))
        missile.x += (math.cos(red)) * 3
        missile.y += (math.sin(red)) * 3
        rect =Rect(missile.topleft,(11,35))
        if shooter_ship.actor.colliderect(rect):
            shooter_ship.hp -= 1
            if shooter_ship.hp ==0:
                status= 3 + (3 * now_stage)
            enemy_ship.missiles.remove(missile)
    return status,shooter_ship

#自機のミサイル
def shooter_missile(status,enemy_ship, shooter_ship):
    now_stage = (status - 1) // 3
    for missile in shooter_ship.missiles:
        missile.y -=10
        rect =Rect(missile.topleft,(16,22))
        if enemy_ship.actor.colliderect(rect):
            enemy_ship.hp -= 1
            if enemy_ship.hp ==0:
                status = 2 + (3 * now_stage)
            shooter_ship.missiles.remove(missile)
    return status,enemy_ship

def draw():
    #SPACE SHOOTER
    if 3 <= status <= 9 :
        space_shooter_draw(status,enemy_ship,shooter_ship)

def update():
    #SPACE SHOOTER
    if status ==4 or status == 7:
        status,enemy_ship,shooter_ship,eshot = space_shooter_update(status,enemy_ship,shooter_ship,eshot)
    
def on_key_down(key):
    #####　SPACE SHOOTER　##########################################################################
    #ゲーム選択
    if key == keys.A:
        if status ==2:
            shooter_ship = create_shooter()
            enemy_ship = create_enemy()
            status = 3

    #ゲームスタート
    if key == keys.RETURN:
        if status == 3 or status == 6:
            shooter_ship = create_shooter()
            enemy_ship = create_enemy()
            status = 4
        elif status == 5 or status == 9:
            shooter_ship = create_shooter()
            enemy_ship = create_enemy()
            status = 7

    #ミサイル発射
    if key == keys.SPACE:
        if status ==4 or status == 7:
            shooter_ship.missiles.append(Actor('smissile.png',shooter_ship.actor.pos))

    #選択画面へ戻る
    if key == keys.P:
        if status ==3 or status == 5 or status ==6 or status == 8 or status == 9:
            status =2
    


