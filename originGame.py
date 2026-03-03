import pgzrun
import random
import math
from dataclasses import dataclass

#画面のサイズ
WIDTH = 800
HEIGHT = 600

status = 1

turn1 =False
turn2 =False
Turn3=False
#星
star = []
for i in range(30):
    rect =Rect((random.randrange(WIDTH),random.randrange(HEIGHT)),(2,2))
    star .append(rect)

moon_lander = Actor('rhome',center=(620,200))
space_shooter = Actor('shome',center=(185,200))
no_touch_game = Actor('ghome',center=(400,200))
shooting_surival = Actor('hhome',center=(185,450))
air_hockey_1 = Actor('bhome1',center=(670,450))
air_hockey_2 = Actor('bhome2',center=(570,450))
air_hockey_3 = Actor('bhome3',center=(620,450))
    
#SPACE SHOOTER　宣言
@dataclass
class space_shooter_enemy_record:
    actor: object
    hp: int
    missiles:list

def create_shooter():
    return space_shooter_enemy_record(
    actor=Actor('shooter.png',(400,500)),
    hp=10,
    missiles=[]
)
shooter_ship = create_shooter()

def create_enemy():
    return space_shooter_enemy_record(
    actor=Actor('eship.png',(400,100)),
    hp=1,
    missiles=[]
)
enemy_ship = create_enemy()

ship_table = [shooter_ship, enemy_ship]

turn =False
eshot = 60






#MOON LANDER　宣言
@dataclass 
class moon_lander_setting_record:
    stage:int
    acceleration:float
    speed:float

moon_lander_table = [moon_lander_setting_record(1, -0.1, 1.0),
                     moon_lander_setting_record(2, -0.2, 1.0),
                     moon_lander_setting_record(3, -0.3, 1.5)]

@dataclass
class moon_lander_rocket_record:
    actor:object
    speed:float

def create_rocket():
    actor = Actor('rocket',center=(400,300))
    actor.angle = 0
        
    return moon_lander_rocket_record(
        actor = actor,
        speed = 0
        )

rocket = create_rocket()

anime_r=animate(None)

#SHOOTING SURVIVER 宣言
map_data=[[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
          [1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0],
          [1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0],
          [0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0],
          [0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0],
          [0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,0],
          [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
          [1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
          [0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1],
          [0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

@dataclass
class shooting_survival_record:
        actor:str
        actor_direction:bool
        missiles:list
        missiles_x:int
        missiles_y:int

        
shooting_survival_missiles_table = [shooting_survival_record("player",0,[],   0, -10),
                                    shooting_survival_record("player",0,[],   0,  10),
                                    shooting_survival_record("player",0,[], -10,   0),
                                    shooting_survival_record("player",0,[],  10,   0),
                                    shooting_survival_record("enemy" ,0,[],   0, -10),
                                    shooting_survival_record("enemy" ,0,[],   0,  10),
                                    shooting_survival_record("enemy" ,0,[], -10,   0),
                                    shooting_survival_record("enemy" ,0,[],  10,   0)]




hock_data=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
goal_data=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]]
map_giza=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#player
location1 =[0,1]
player_hp = 10
#enemy
location2 =[13,18]
enemy_hp =10
#player
player=Actor('player',topleft=(40,0))
#enemy
enemy=Actor('enemy',topleft=(720,520))
#遊び方
juuzi=Actor('juuzi.png',center=(200,400))
#床のタイル
floor=Actor('floor',topleft=(0,0))
#箱
box=Actor('box',topleft=(0,0))
box2=Actor('box2',topleft=(0,0))
#ボール
boal=Actor('boal',topleft=(400,40))
#パック
pack1=Actor('pack1',topleft=(120,300))
pack2=Actor('pack2',topleft=(640,300))
#ゴール
goal=Actor('goal',topleft=(0,0))
apoint =0
bpoint=0
#出口の看板
#exit =Actor('exit',topleft=(700,490))
#キーボード
#gizagizaの宣言
#床のタイル
floorgi=Actor('floor',topleft=(0,0))
#箱
boxgi=Actor('box',topleft=(0,0))
#ボール
boalgi=Actor('boal',center=(0,300))



#####　ガイドテキスト　############################################################################
def game_start_guide():
    #初めのガイド
    start_guide = [("start",(550,150),"click Enter",(650,150),'RED'),
                   ("back" ,(550,100),"click P"    ,(650,100),'YELLOW')]
    #初めのガイド
    for guide,gpos,click,cpos,g_color in start_guide:
        screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

def game_middle_guide():
    #ゲームクリア時のガイド
    end_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                 ("next", (550, 150), "click Enter", (650, 150), 'RED'   )]
    
    #ゲームクリア時のガイド
    for guide,gpos,click,cpos,g_color in end_guide:
        screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

def game_end_guide():
    #ゲームクリア時のガイド
    end_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                 ("next", (550, 150), "click Enter", (650, 150), 'RED'   )]
    
    #終わりのガイド
    for guide,gpos,click,cpos,g_color in end_guide:
        if guide =="menu":
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

def game_over_guide():
    #ゲームオーバー時のガイド
    game_over_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                       ("restart", (550, 150), "click Enter", (650, 150), 'RED'   )]
    
    #ゲームオーバー時のガイド
    for guide,gpos,click,cpos,g_color in game_over_guide:
        screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

#####　ホーム画面(DRAW) ###########################################################################
def home():
    screen.draw.text('S P A C E  G A M E S',(160,290),color = 'WHITE',gcolor = 'YELLOW',fontsize=72)
    screen.draw.text('click SPACE',(335,400),color = 'WHITE',gcolor = 'RED',fontsize=30)

    
#####　メニュー画面(DRAW)　########################################################################
def menu():
    #メニュー画面のゲームのタイトル
    menu_title = [("SPACE SHOOTER"    , (130, 280), "click A", (150, 310)),
                  ("MOON LANDER"      , (570, 280), "click C", (590, 310)),
                  ("SHOOTING SURVIVAL", (120, 500), "click D", (150, 520)),
                  ("AIR HOCKEY"       , (580, 500), "click E", (590, 530)),
                  ("NO TOUGH GAME"    , (345, 280), "click B", (370, 310))]
    #メニュー画面の画像
    menu_picture=[moon_lander,
                      space_shooter,
                      no_touch_game,
                      shooting_surival,
                      air_hockey_1,
                      air_hockey_2,
                      air_hockey_3]

    #タイトル
    screen.draw.text('S P A C E G A M E S',(160,50),color = 'WHITE',gcolor = 'YELLOW',fontsize=72)

    #メニュー画面のゲームのタイトル
    for title, tpos, click, cpos in menu_title:
        screen.draw.text(title, tpos, color='WHITE', gcolor='RED', fontsize=20)
        screen.draw.text(click, cpos, color='WHITE', gcolor='YELLOW', fontsize=30)

    #メニュー画面の画像
    for picture in menu_picture:
        picture.draw()

    #screen.draw.text('ONE PLAYER',(260,100),color = 'WHITE',gcolor = 'RED',fontsize=60)
    
    
#####　SPACE SHOOTER(DRAW)　#######################################################################
def space_shooter_draw(status,enemy_ship,shooter_ship):
    #SPACE SHOOTER オープニング
    if status == 3:
        screen.draw.text('S P A C E  S H O O T E R',(120,290),color='WHITE',gcolor = 'YELLOW',fontsize =72)
        game_start_guide()

        shooter_ship.actor.draw()
        enemy_ship.actor.draw()

    else:
        space_shooter_battle_draw(status,enemy_ship, shooter_ship)
    

                
def space_shooter_battle_draw(status,enemy_ship, shooter_ship):
    #SPACE SHOOTER HPの描写
    space_shooter_hp = [(f'Enemy HP = {enemy_ship.hp}'    ,(50 ,50)),
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
        for text,pos in space_shooter_hp:
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
    space_shooter_move_shooter(shooter_ship)
    
    #敵を左右に動かす
    space_shooter_move_enemy(status,enemy_ship)       


    #敵のミサイルの角度        
    if eshot ==0:
        space_shooter_enemy_missile_angle(enemy_ship,shooter_ship)
        eshot = 60 #時間をリセット 
    else:
        eshot -=1
        

    #敵のミサイル
    status,shooter_ship = space_shooter_enemy_missile(status,enemy_ship, shooter_ship)
        

    #自機のミサイル
    status,enemy_ship = space_shooter_shooter_missile(status,enemy_ship, shooter_ship)

    return status,enemy_ship,shooter_ship,eshot


#自機のキー操作
def space_shooter_move_shooter(shooter_ship):
    if keyboard.left:
        if shooter_ship.actor.x>47:
            shooter_ship.actor.x -= 3
    if keyboard.right:
        if shooter_ship.actor.x < WIDTH-47:
            shooter_ship.actor.x += 3

def space_shooter_enemy_missile_angle(enemy_ship,shooter_ship):
    angle = enemy_ship.actor.angle_to(shooter_ship.actor)
    missile1 = Actor('emissile.png',(enemy_ship.actor.x-25,enemy_ship.actor.y+10))
    missile2 = Actor('emissile.png',(enemy_ship.actor.x+25,enemy_ship.actor.y+10))
    missile1.angle =90 +angle
    missile2.angle =90 +angle
    enemy_ship.missiles.append(missile1)
    enemy_ship.missiles.append(missile2)

#敵を左右に動かす
def space_shooter_move_enemy(status,enemy_ship):
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
def space_shooter_enemy_missile(status,enemy_ship, shooter_ship):
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
def space_shooter_shooter_missile(status,enemy_ship, shooter_ship):
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
#####　MOON LANDER(DRAW)　#########################################################################
def moon_lander_draw(status):
    #MOON LANDER　オープニング
    moon_lander_draw_stage()
    
    if status == 10:
        for i in range(20):
            screen.draw.rect(star[i],'WHITE')
        for i in range(50):
            screen.draw.line((350-i*3,550+i),(450+i*3,550+i),'GRAY')
        for i in range(10):
            screen.draw.circle(rocket.actor.midbottom,i+1,(255,i*20,0))
            screen.draw.text("Moon Lander",(250,100),owidth=1.5,ocolor ='YELLOW',color ='BLACK',fontsize=64)
        game_start_guide()
    else:
        moon_lander_play_draw(status)
    
def moon_lander_play_draw(status):
    global key_flg
    now_stage = ((status + 1) // 3) - 3 #今のステージを計算
    if status == 11 or status == 14 or status == 17:
        screen.draw.text(f'STAGE {now_stage}',(110,300),color ='YELLOW',fontsize =64)
        if key_flg:
            for i in range(10):
                screen.draw.circle(rocket.actor.midbottom,i+1,(255,i*20,0))

    elif status == 12 or status == 15 or status == 18:
        if now_stage <= 2:
            screen.draw.text("GAME CLEAR",(40,300),owidth=1.5,ocolor='YELLOW',color='BLACK',fontsize=64)
            game_middle_guide()
        else:
            screen.draw.text("COMPLETE",(60,300),owidth=1.5,ocolor='YELLOW',color='BLACK',fontsize=64)
            game_end_guide()
            
    elif status == 13 or status == 16 or status == 19:
        screen.draw.text("GAME OVER",(50,300),owidth=1.5,ocolor='RED',color='BLACK',fontsize=64)
        game_over_guide()

def moon_lander_draw_stage():
    for i in range(20):
        screen.draw.rect(star[i],'WHITE')

    for i in range(50):
        screen.draw.line((350-i*3,550+i),(450+i*3,550+i),'GRAY')
    rocket.actor.draw()
    
    
        
#####　MOON LANDER(UPDATE)　#######################################################################
def moon_lander_update(rocket,status):
    global key_flg
    now_stage = ((status - 2) // 3) - 2
    if keyboard.up:
        key_flg = True
        acceleration = moon_lander_table[now_stage - 1].acceleration
    else:
        key_flg = False
        acceleration = -(moon_lander_table[now_stage - 1].acceleration)
    rocket.speed += acceleration
    rocket.actor.y += rocket.speed
    if rocket.actor.y > 500:
        if rocket.speed < moon_lander_table[now_stage - 1].speed:
            status = 9  + (now_stage * 3) #STAGE1なら12,STAGE2なら15,STAGE3なら18
            
        else:
            status = 10 + (now_stage * 3) #STAGE1なら13,STAGE2なら16,STAGE3なら19
            anime_r =animate(rocket.actor, 'bounce_start_end',1,angle=45)

    return rocket,status
#####　SHOOTING SURVIVAL(DRAW)　###################################################################
def shooting_survival_draw(status,space_shooter_missiles_table):
    #SHOOTING SURVIVAL　オープニング
    if status ==20:
        shooting_survival_draw_stage()
        screen.draw.text('SHOOTING SURVIVAL',(85,200),color='WHITE',gcolor = 'RED',fontsize =72)
        game_start_guide()
        
    #ゲーム画面
    elif status ==21:
        #ステージの描写
        shooting_survival_draw_stage()
        #HP の描写
        shooting_survival_draw_hp()
        
        #ミサイルの描写
        shooting_survival_draw_missiles(space_shooter_missiles_table)
        
        #終わりのガイド
        game_end_guide()


    #結果
    elif status == 22 or status == 23:
        shooting_survival_winner_draw(status)
        game_over_guide()
        
def shooting_survival_draw_stage():
    for y in range(15):
        for x in range(20):
            if map_data[y][x] !=0:
                box2.topleft=(40*x,40*y)
                box2.draw()
    player.draw()
    enemy.draw()

def shooting_survival_winner_draw(status):
    shooting_survival_draw_stage()
    win_player = status - 21 #Player1が勝ったら1,Player2が勝ったら2
    screen.draw.text(f'PLAYER {win_player} WIN',(85,200),color='WHITE',gcolor = 'RED',fontsize =72)

    game_over_guide()

def shooting_survival_draw_hp():
    #SHOOTING SURVIVAL HP
    shooting_survival_hp = [(f'Player1 HP = {player_hp}',(100,15)),
                            (f'Player2 HP = {enemy_hp}' ,(500,15))]
    #HPの描写
    for text,pos in shooting_survival_hp:
        screen.draw.text(text,pos,color='YELLOW',fontsize = 32)

def shooting_survival_draw_missiles(table):
    for record in table:
        for missile in record.missiles:
            missile.draw()
    
    
    
    
#####　SHOORING SURVIVAL(UPDATE)　#################################################################
#弾の衝突判定
def shou(a,b):
    for y in range(15):
        for x in range(20):
            if map_data[y][x] !=0:
                
                if ((x*40 < a)
                and (a<x*40+40) 
                and (y*40<b) 
                and (b< y*40+40)):
                    return 1
#playerのミサイル
def shooting_survival_missiles_update(record,enemy_hp,player_hp,status):
    for missile in record.missiles:
        missile.x += record.missiles_x
        missile.y += record.missiles_y
        rect = Rect(missile.topleft, (15, 20))
        x = missile.x
        y = missile.y
        
        if shou(x, y) == 1:
            record.missiles.remove(missile)

        if record.actor == "player":
            
            if enemy.colliderect(rect):
                enemy_hp -= 1
                record.missiles.remove(missile)
                
                if enemy_hp == 0:
                    status = 22
            
        else:
            if player.colliderect(rect):
                player_hp -= 1
                record.missiles.remove(missile)
                
                if player_hp == 0:
                    status = 23
            
                
    return  enemy_hp,player_hp,status

#####　AIR HOCEKY(DRAW)　##########################################################################
def air_hockey_draw(status):
    air_hockey_draw_stage()

    #AIR HOCEKY オープニング
    if status==26:
        screen.draw.text('AIR HOCKEY',(230,200),color = 'WHITE',gcolor = 'YELLOW',fontsize=72)
        game_start_guide()

    #ゲーム画面
    elif status == 27:
        air_hockey_draw_point()
        

    elif status == 28 or status == 29:
        air_hockey_goal_draw(status)
        game_middle_guide()
        
    elif status == 30 or status == 31:
        air_hockey_Winner_draw(status)
        game_end_guide()
        
def air_hockey_draw_stage():
    for y in range(15):
        for x in range(20):
            floor.topleft=(40*x,40*y)
            floor.draw()
            if hock_data[y][x] ==1:
                box.topleft=(40*x,40*y)
                box.draw()
    for y in range(3):
        for x in range(20):
            if goal_data[y][x] ==3:
                goal.topleft=(40*x,200*(y-1))
                goal.draw()
    boal.draw()
    pack1.draw()
    pack2.draw()

def air_hockey_goal_draw(status):
    get_goal_player = status % 2  #Player1なら0,Player2なら1
    gcolor = ['RED','YELLOW']
    screen.draw.text('GOAL!', (160,200), color = 'WHITE', gcolor = gcolor[get_goal_player], fontsize=72)
    
def air_hockey_Winner_draw(status):
    get_goal_player = status % 2  #Player1なら0,Player2なら1
    gcolor = ['RED','YELLOW']
    screen.draw.text(f'Player {get_goal_player + 1} win',(160,200),color = 'WHITE',gcolor = gcolor[get_goal_player],fontsize=72)
    

def air_hockey_draw_point():
    #AIR HOCKEY POINTの描写
    air_hockey_point = [(f'A point = {apoint}', (50 ,50)),
                        (f'B point = {bpoint}', (600,50))]
    #Pointの描写
    for text,pos in air_hockey_point:
        screen.draw.text(text,pos,color='YELLOW',fontsize = 32)
    
    
    
#####　AIR HOCKEY(UPDATE)　########################################################################
def air_hockey_update():
    pass
#####　壁に当てちゃだめゲーム(DRAW)　##############################################################
def no_touch_game_draw(status):
    if status ==38:
        screen.draw.text("壁にあてちゃダメゲーム", (220, 250), fontname="ipaexg.ttf", color="YELLOW", fontsize=32)
        game_start_guide()
    elif status == 39:
        no_touch_game_draw_stage()
        screen.draw.text("UPキー：上へ", (50, 600), fontname="ipaexg.ttf", color="YELLOW", fontsize=32)
        screen.draw.text("DOWNキー：下へ", (100, 600), fontname="ipaexg.ttf", color="YELLOW", fontsize=32)
    elif status ==40:
        no_touch_game_draw_stage()
        screen.draw.text("ダメ～", (220, 250), fontname="ipaexg.ttf", color="RED", fontsize=32)
                        
    elif status ==41:
        no_touch_game_draw_stage()
        screen.draw.text('goal',(160,200),color = 'WHITE',gcolor = 'BLUE',fontsize=72)

def no_touch_game_draw_stage():
    for y in range(15):
            for x in range(20):
                floorgi.topleft=(40*x,40*y)
                floorgi.draw()
                if map_giza[y][x] ==1:
                    boxgi.topleft=(40*x,40*y)
                    boxgi.draw()
                    boalgi.draw()
#####　壁に当てちゃだめゲーム(UPDATE)　############################################################
def no_touch_game_update():
    pass

def atari(boalgi,status):
    if boalgi.x>0:
        if boalgi.y<60 or boalgi.y>540:
         status=40
    if boalgi.x>60:
        if boalgi.y<100 or boalgi.y>500:
            status=40

    if boalgi.x>140:
        if boalgi.y<140 or boalgi.y>460:
             status=40

    if boalgi.x>220:
        if boalgi.y<180 or boalgi.y>420:
            status=40

    if boalgi.x>300:
        if boalgi.y<220 or boalgi.y>380:
            status=40

    if boalgi.x>380:
        if boalgi.y<260 or boalgi.y>340:
            status=40
    if boalgi.x>780:
        status=41
    return status
###################################################################################################

#絵の描画
def draw():
    global status,enemy,player,player_hp,enemy_hp,apoint,bpoint
    global enemy_ship,shooter_ship
        
    if status < 31 or status == 33 or status >35 :
        screen.clear()
    
    #星を描く
    if status <30 :
        for i in range(len(star)):
            screen.draw.rect(star[i],'WHITE')
   
    #ホーム
    if status ==1:
        home()


    #選択画面
    elif status == 2:
        menu()

        
    #SPACE SHOOTER
    elif 3 <= status <= 9 :
        space_shooter_draw(status,enemy_ship,shooter_ship)
        

    #MOON LANDER　
    elif 10 <= status <= 19:
        moon_lander_draw(status)


    #SHOOTING SURVIVAL
    elif 20 <= status <=23:
        shooting_survival_draw(status,space_shooter_missiles_table)
        
    

    #AIR HOCKEY
    elif 26 <= status <= 31:
        air_hockey_draw(status)
        

    #壁に当てちゃだめゲーム
    elif 38 <= status <= 41 :
        no_touch_game_draw(status)

        


def update():
    global status,i,j,k,l,a,b,c,d,enemy_hp,player_hp
    global speed,key_flg,anime_r,rocket
    global turn1,turn2,bx,by,px,py,status,apoint,bpoint,Turn3
    global enemy_ship,shooter_ship,turn,eshot
    
    for i in range(len(star)):
        star[i].y += i
        if star[i].y > HEIGHT:
            star[i].y =0


    #SPACE SHOOTER
    if status ==4 or status == 7:
        status,enemy_ship,shooter_ship,eshot = space_shooter_update(status,enemy_ship,shooter_ship,eshot)
        

    #MOON LANDER
    if status == 11 or status == 14 or status == 17:
        rocket,status = moon_lander_update(rocket,status)

    #MAZE
    elif status ==21:

        for record in space_shooter_missiles_table:
            if record.actor_direction == 1:
                enemy_hp, player_hp, status = shooting_survival_missiles_update(
                    record, enemy_hp, player_hp, status
                )
    #bound
    elif status == 27:
            
        
        if turn1 :
            boal.x += 10
            if (pack2.x-35) == boal.x-5 and (boal.y+60) >pack2.y-20 and (boal.y+60) < (pack2.y +140):
                turn1=False
            elif (pack1.x-35) == boal.x-5 and (boal.y+60) >pack1.y-20 and (boal.y+60) < (pack1.y +140):
                turn1=False
            elif (boal.x > 740 and boal.y<220 and boal.y>40)or(boal.x > 740 and boal.y>380 and boal.y<560):
                turn1 =False
            elif (boal.x>780 and boal.y >160 and boal.y <400):
                apoint +=1
                if apoint>=5:
                    status=30
                else:
                    status=28
            
        else:
            boal.x -= 10
            if (pack1.x+35) == boal.x+5 and (boal.y+60) >pack1.y-20 and (boal.y+60) < (pack1.y +140):
                turn1=True
            elif (pack2.x+35) == boal.x+5 and (boal.y+60) >pack2.y-20 and (boal.y+60) < (pack2.y +140):
                turn1=True
            elif (boal.x < 60 and boal.y<220 and boal.y>40)or(boal.x < 60 and boal.y>380 and boal.y<560):
                turn1 =True
            elif (boal.x < 20 and boal.y >160 and boal.y <400):
                bpoint +=1
                if bpoint >=5:
                    status =31
                else:
                    status = 29
                                                 
                                                 
    
        if turn2 :
            boal.y += 10
            if pack1.y == boal.y+60 and boal.x >60 and boal.x < 220:
                turn2=False
            elif pack2.y == boal.y+60 and boal.x >580 and boal.x < 740:
                turn2=False    
            elif boal.y > HEIGHT-60:
                turn2 =False
            
        else:
            boal.y -= 10
            if pack1.y+60 == boal.y and (boal.x) >60 and boal.x < 220:
                turn2=True
            elif pack2.y+60 == boal.y and (boal.x) >580 and boal.x < 740:
                turn2=True
            elif boal.y <60:
                turn2 =True
        #パック１の操作

        if keyboard.W:
            if pack1.y>120:
                pack1.y -= 5
                px=pack1.x
        if keyboard.S:
            if pack1.y < HEIGHT-80:
                pack1.y += 5
                py=pack1.y

        if keyboard.UP:
            if pack2.y>120:
                pack2.y -= 5
                px=pack2.x
        if keyboard.DOWN:
            if pack2.y < HEIGHT-80:
                pack2.y += 5
                py=pack2.y
                
    elif status ==38:
        if keyboard.SPACE:
            status=39
    

    elif status ==39:
        boalgi.x +=1
        if Turn3 :
            boalgi.y -=5
            status = atari(boalgi,status)
        else:
            boalgi.y += 5
            status = atari(boalgi,status)
        
        if keyboard.UP:
            Turn3 = True
        if keyboard.DOWN:
            Turn3 = False
            
    elif status ==40:
        if keyboard.SPACE:
            boalgi.center=(0,300)
            status=39

    
    

def on_key_down(key):
    global status
    global speed
    global a,b,c,d,o,j,k,l,player_hp,enemy_hp
    global location1,location2,player,enemy,p_missile,s_missile,apoint,bpoint
    global shooter_ship,enemy_ship
    global rocket

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

    

    
#####　MOON LANDER　###########################################################################################
    #ゲーム選択
    if key == keys.B:
        if status ==2:
            rocket = create_rocket()
            status = 10

    #ゲームスタート
    if key == keys.SPACE and anime_r.running != True:
        #STAGE1
        if status == 10 or status == 13:
            rocket = create_rocket()
            
            status =11
        #STAGE2    
        elif status == 12 or status ==16:
            rocket = create_rocket()
            
            status =14
        #STAGE3    
        elif status == 15 or status == 19:
            rocket = create_rocket()

            status =17

    #選択画面へ戻る
    if key == keys.P:
        if 10 <= status <= 19:
            status =2
    
    
###################################################################################################


    if key == keys.SPACE:
        if status ==1:
            status = 2
        
        elif status ==20:
            player_hp=10
            enemy_hp=10
            s_missiles=[]
            e_missiles=[]
            player=Actor('player',topleft=(40,0))
            enemy=Actor('enemy',topleft=(720,520))
            
            location1 =[0,1]
            location2 =[13,18]
            status =21
        elif status ==22:
            player_hp=10
            enemy_hp=10
            s_missiles=[]
            e_missiles=[]
            location1 =[0,1]
            location2 =[13,18]
            player=Actor('player',topleft=(40,0))
            enemy=Actor('enemy',topleft=(720,520))
            status=21
        elif status ==23:
            player_hp=10
            enemy_hp=10
            s_missiles=[]
            e_missiles=[]
            location1 =[0,1]
            location2 =[13,18]
            player=Actor('player',topleft=(40,0))
            enemy=Actor('enemy',topleft=(720,520))
            status =21
        elif status==26:
            turn1 =False
            turn2 =False
            boal.topleft=(400,300)
            status=27
        elif status ==28:
            turn1 =False
            turn2 =False
            boal.topleft=(400,300)
            status =27
        elif status == 29:
            turn1 =True
            turn2 =True
            boal.topleft=(400,300)
            status =27
    
    #戻る
    if key == keys.P:
        if status ==2:
            status =1
        elif status == 20:
            status =2
        elif status ==21:
            status=2
        elif status == 22:
            status =2
        elif status == 23:
            status =2
        elif status == 24:
            status =3
        elif status == 25:
            status =10
        elif status ==26:
            status=2
        elif status==28:
            status=26
        elif status ==29:
            status=26
        elif status ==30:
            apoint =0
            bpoint=0
            #パック
            pack1=Actor('pack1',topleft=(120,300))
            pack2=Actor('pack2',topleft=(640,300))
            status =2
        elif status==31:
            apoint =0
            bpoint=0
            #パック
            pack1=Actor('pack1',topleft=(120,300))
            pack2=Actor('pack2',topleft=(640,300))
            status=2
        elif status == 40:
            status =2
        elif status == 41:
            status=2
        
    if key == keys.E:
        if status ==2:
            boalgi.center=(0,300)
            status=38    
            
    if key == keys.A:
            
        if status == 21:
            #プレイヤーが端でなければ
            if location1[1] >= 1:
                if map_data[location1[0]][location1[1]-1] != 1:
                    location1[1] -= 1
                    player.x -=40
    
    if key ==keys.W:
        if status == 21:
            #プレイヤーが上端でなければ
            if location1[0] >= 1:
                #プレイヤーの進む方向がボックスでなければ進
                if map_data[location1[0]-1][location1[1]] !=1:
                    location1[0] -= 1
                    player.y -= 40

    if key == keys.C:
        if status ==2:
            location1 =[0,1]
            location2 =[13,18]
            player=Actor('player',topleft=(40,0))
            enemy=Actor('enemy',topleft=(720,520))
            status=20
            

    if key == keys.S:
        if status == 21:
            #プレイヤーが下端でなければ
            if location1[0] <= 12:
                if map_data[location1[0]+1][location1[1]] != 1:
                    location1[0] += 1
                    player.y +=40

    
    if key == keys.D:
        if status ==2:
            turn1 =False
            turn2 =False
            boal.topleft=(400,300)
            status=26
        elif status == 21:
            #プレイヤーが端でなければ
            if location1[1] <= 18:
                if map_data[location1[0]][location1[1]+1] != 1:
                    location1[1] += 1
                    player.x +=40
    if key == keys.T:
        space_shooter_missiles_table[0].missiles.append(Actor('pmissile1.png',player.pos))
        space_shooter_missiles_table[0].actor_direction = 1

    if key == keys.G:
        space_shooter_missiles_table[1].missiles.append(Actor('pmissile2.png',player.pos))
        space_shooter_missiles_table[1].actor_direction = 1
        
    if key == keys.F:
        space_shooter_missiles_table[2].missiles.append(Actor('pmissile3.png',player.pos))
        space_shooter_missiles_table[2].actor_direction = 1
        
    if key == keys.H:
        space_shooter_missiles_table[3].missiles.append(Actor('pmissile4.png',player.pos))
        space_shooter_missiles_table[3].actor_direction = 1
    
    if key ==keys.UP:
        #プレイヤーが上端でなければ
        if location2[0] >= 1:
            if status == 21:
                #プレイヤーの進む方向がボックスでなければ進
                if map_data[location2[0]-1][location2[1]] !=1:
                    location2[0] -= 1
                    enemy.y -= 40
    
    if key == keys.DOWN:
        if status == 21:
            #プレイヤーが下端でなければ
            if location2[0] <= 12:
                if map_data[location2[0]+1][location2[1]] != 1:
                    location2[0] += 1
                    enemy.y +=40

    if key == keys.LEFT:
        if status == 21:
            #プレイヤーが端でなければ
            if location2[1] >= 1:
                if map_data[location2[0]][location2[1]-1] != 1:
                    location2[1] -= 1
                    enemy.x -=40
                              
    if key == keys.RIGHT:
        if status == 21:
            #プレイヤーが端でなければ
            if location2[1] <= 18:
                if map_data[location2[0]][location2[1]+1] != 1:
                    location2[1] += 1
                    enemy.x +=40
    if key == keys.KP5:
        space_shooter_missiles_table[4].missiles.append(Actor('emissile1.png',enemy.pos))
        space_shooter_missiles_table[4].actor_direction = 1

    if key == keys.KP2:
        space_shooter_missiles_table[5].missiles.append(Actor('emissile2.png',enemy.pos))
        space_shooter_missiles_table[5].actor_direction = 1
        
    if key == keys.KP1:
        space_shooter_missiles_table[6].missiles.append(Actor('emissile3.png',enemy.pos))
        space_shooter_missiles_table[6].actor_direction = 1
        
    if key == keys.KP3:
        space_shooter_missiles_table[7].missiles.append(Actor('emissile4.png',enemy.pos))
        space_shooter_missiles_table[7].actor_direction = 1                                 

pgzrun.go()
