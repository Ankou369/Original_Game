import pgzrun
import random
import math

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
#SPACE SHOOTER　宣言
shooter = Actor('shooter.png',(400,500))
eship =Actor('eship.png',(400,100))
shooter_hp =10
eship_hp =30
s_missiles = []
turn =False
eshot = 60
e_missiles =[]
#MOON LANDER　宣言
rocket =Actor('rocket',center=(400,300))
                      
moon_lander = Actor('rhome',center=(620,200))
space_shooter = Actor('shome',center=(185,200))
no_touch_game = Actor('ghome',center=(400,200))
shooting_surival = Actor('hhome',center=(185,450))
air_hockey_1 = Actor('bhome1',center=(670,450))
air_hockey_2 = Actor('bhome2',center=(570,450))
air_hockey_3 = Actor('bhome3',center=(620,450))

speed =0
acceleration =0.1
key_flg =False
anime_r=animate(None)
#SHOOTING SURVIVER 宣言
p_missiles1 = []
p_missiles2 = []
p_missiles3 = []
p_missiles4 = []
e_missiles1 = []
e_missiles2 = []
e_missiles3 = []
e_missiles4 = []
a=0
b=0
c=0
d=0
o=0
j=0
k=0
l=0
#map
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


#絵の描画
def draw():
    global status,eship,enemy,player,player_hp,enemy_hp,apoint,bpoint

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

    #SPACE SHOOTER HPの描写
    space_shooter_hp = [(f'Enemy HP = {eship_hp}'    ,(50 ,50)),
                        (f'Shooter HP = {shooter_hp}',(600,50))]

    #SHOOTING SURVIVAL HPの描写
    shooting_survival_hp = [(f'Player1 HP = {player_hp}',(100,15)),
                            (f'Player2 HP = {enemy_hp}' ,(500,15))]

    #AIR HOCKEY POINTの描写
    air_hockey_point = [(f'A point = {apoint}', (50 ,50)),
                        (f'B point = {bpoint}', (600,50))]


    #初めのガイド
    start_guide = [("start",(550,150),"click Enter",(650,150),'RED'),
                   ("back" ,(550,100),"click P"    ,(650,100),'YELLOW')]
    #ゲームクリア時のガイド
    end_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                 ("next", (550, 150), "click Enter", (650, 150), 'RED'   )]
    #ゲームオーバー時のガイド
    game_over_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                       ("restart", (550, 150), "click Enter", (650, 150), 'RED'   )]
        
    if status < 31 or status == 33 or status >35 :
        screen.clear()
    
    #星を描く
    if status <30 :
        for i in range(len(star)):
            screen.draw.rect(star[i],'WHITE')
   
    #ホーム
    if status ==1:

        screen.draw.text('S P A C E  G A M E S',(160,290),color = 'WHITE',gcolor = 'YELLOW',fontsize=72)
        screen.draw.text('click SPACE',(335,400),color = 'WHITE',gcolor = 'RED',fontsize=30)



    #選択画面
    elif status == 2:
        
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


        
    #SPACE SHOOTER オープニング
    elif status == 3:
        #SpaceShooterタイトル
        screen.draw.text('S P A C E  S H O O T E R',(120,290),color='WHITE',gcolor = 'YELLOW',fontsize =72)

        #初めのガイド
        for guide,gpos,click,cpos,g_color in start_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)        


                
    #SPACE SHOOTER STAGE1
    elif status ==4:
        screen.draw.text("STAGE 1",(300,300),color ='YELLOW',fontsize =64)

        #ミサイルの描写
        for missile in s_missiles:
            missile.draw()
        for missile in e_missiles:
            missile.draw()
        #HPの描写
        for text,pos in space_shooter_hp:
            screen.draw.text(text,pos,color='YELLOW',fontsize = 32)
            
    elif status == 5:
        screen.draw.text('G A M E  C L E A R',(310,290),color ='WHITE',gcolor ='YELLOW',fontsize=32)

        #ゲームクリア時のガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

    elif status == 6:
        screen.draw.text('G A M E  O V E R',(310,290),color ='WHITE',gcolor ='RED',fontsize=32)

        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)



    #SPACE SHOOTER STAGE2
    elif status == 7:
        screen.draw.text("STAGE 2",(110,300),color ='YELLOW',fontsize =64)
        for missile in s_missiles:
            missile.draw()
        for missile in e_missiles:
            missile.draw()
        #HPの描写
        for text,pos in space_shooter_hp:
            screen.draw.text(text,pos,color='YELLOW',fontsize = 32)
            
    elif status == 8:
        screen.draw.text('G A M E  C L E A R',(310,290),color ='WHITE',gcolor ='YELLOW',fontsize=32)

        #終わりのガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            if guide =="menu":
                screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
                screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

    elif status == 9:
        screen.draw.text('G A M E  O V E R',(310,290),color ='WHITE',gcolor ='RED',fontsize=32)

        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)


            
    #MOON LANDER　オープニング	
    elif status == 10:
        for i in range(20):
            screen.draw.rect(star[i],'WHITE')
        for i in range(50):
            screen.draw.line((350-i*3,550+i),(450+i*3,550+i),'GRAY')
        for i in range(10):
            screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
            screen.draw.text("Moon Lander",(250,100),owidth=1.5,ocolor ='YELLOW',color ='BLACK',fontsize=64)

        #初めのガイド
        for guide,gpos,click,cpos,g_color in start_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)



    #MOON LANDER STAGE1
    elif status ==11:
        screen.draw.text("STAGE 1",(110,300),color ='YELLOW',fontsize =64)
        if key_flg:
            for i in range(10):
                screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))

    elif status ==12:
        screen.draw.text("GAME CLEAR",(40,300),owidth=1.5,ocolor='YELLOW',color='BLACK',fontsize=64)

        #ゲームクリア時のガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            
    elif status ==13:
        screen.draw.text("GAME OVER",(50,300),owidth=1.5,ocolor='RED',color='BLACK',fontsize=64)
        
        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)



    #MOON LANDER STAGE2
    elif status ==14:
        screen.draw.text("STAGE 2",(110,300),color ='YELLOW',fontsize =64)
        if key_flg:
            for i in range(10):
                screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
    elif status ==15:
        screen.draw.text("GAME CLEAR",(40,300),owidth=1.5,ocolor='YELLOW',color='BLACK',fontsize=64)

        #ゲームクリア時のガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

    elif status ==16:
        screen.draw.text("GAME OVER",(50,300),owidth=1.5,ocolor='RED',color='BLACK',fontsize=64)
        
        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)



    #MOON LANDER STAGE3
    elif status ==17:
        screen.draw.text("STAGE 3",(110,300),color ='YELLOW',fontsize =64)
        if key_flg:
            for i in range(10):
                screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))

    elif status ==18:
        screen.draw.text("COMPLETE",(60,300),owidth=1.5,ocolor='YELLOW',color='BLACK',fontsize=64)
        #終わりのガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            if guide =="menu":
                screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
                screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        
    elif status ==19:
        screen.draw.text("GAME OVER",(40,300),owidth=1.5,ocolor='RED',color='BLACK',fontsize=64)
        
        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)



    #SHOOTING SURVIVAL
    elif status ==20:
        for y in range(15):
            for x in range(20):
                #floor.topleft=(35*x,35*y)
                #floor.draw()
                if map_data[y][x] !=0:
                    box2.topleft=(40*x,40*y)
                    box2.draw()
        player.draw()
        enemy.draw()
        screen.draw.text('SHOOTING SURVIVAL',(85,200),color='WHITE',gcolor = 'RED',fontsize =72)
        #初めのガイド
        for guide,gpos,click,cpos,g_color in start_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)



    #ゲーム画面
    elif status ==21:
        
        for y in range(15):
            for x in range(20):
                if map_data[y][x] !=0:
                    box2.topleft=(40*x,40*y)
                    box2.draw()
                    
        for missile1 in p_missiles1:
            missile1.draw()
        for missile2 in p_missiles2:
            missile2.draw()
        for missile3 in p_missiles3:
            missile3.draw()
        for missile4 in p_missiles4:
            missile4.draw()
        for missile5 in e_missiles1:
            missile5.draw()
        for missile6 in e_missiles2:
            missile6.draw()
        for missile7 in e_missiles3:
            missile7.draw()
        for missile8 in e_missiles4:
            missile8.draw()
        
        player.draw()
        enemy.draw()
        #終わりのガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            if guide =="menu":
                screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
                screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

        #HPの描写
        for text,pos in shooting_survival_hp:
            screen.draw.text(text,pos,color='YELLOW',fontsize = 32)



    #Player1 勝利時
    elif status ==22:
        for y in range(15):
            for x in range(20):
                if map_data[y][x] !=0:
                    box2.topleft=(40*x,40*y)
                    box2.draw()
        
        player.draw()
        screen.draw.text('PLAYER 1 WIN',(85,200),color='WHITE',gcolor = 'RED',fontsize =72)
        
        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)



    #Player2 勝利時
    elif status ==23:
        for y in range(15):
            for x in range(20):
                if map_data[y][x] !=0:
                    box2.topleft=(40*x,40*y)
                    box2.draw()
        
        enemy.draw()
        screen.draw.text('PLAYER 2 WIN',(85,200),color='WHITE',gcolor = 'RED',fontsize =72)
        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        
    

    #AIR HOCKEY
    elif status==26:
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
        screen.draw.text('AIR HOCKEY',(230,200),color = 'WHITE',gcolor = 'YELLOW',fontsize=72)
        
        #初めのガイド
        for guide,gpos,click,cpos,g_color in start_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            
        boal.draw()
        pack1.draw()
        pack2.draw()
        
    elif status == 27:
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

        #Pointの描写
        for text,pos in air_hockey_point:
            screen.draw.text(text,pos,color='YELLOW',fontsize = 32)
        
        boal.draw()
        pack1.draw()
        pack2.draw()

    elif status ==28:
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
        screen.draw.text('GOAL!',(160,200),color = 'WHITE',gcolor = 'RED',fontsize=72)
        
        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            
        boal.draw()
        pack1.draw()
        pack2.draw()

    elif status ==29:
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
        screen.draw.text('GOAL!',(160,200),color = 'WHITE',gcolor = 'YELLOW',fontsize=72)
        
        #ゲームオーバー時のガイド
        for guide,gpos,click,cpos,g_color in game_over_guide:
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            
        boal.draw()
        pack1.draw()
        pack2.draw()

    elif status==30:
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
        screen.draw.text('Player1 win',(160,200),color = 'WHITE',gcolor = 'RED',fontsize=72)
        
        #終わりのガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            if guide =="menu":
                screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
                screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

        boal.draw()
        pack1.draw()
        pack2.draw()
    



    elif status ==31:
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
        screen.draw.text('Player2 win',(160,200),color = 'WHITE',gcolor = 'RED',fontsize=72)
        #終わりのガイド
        for guide,gpos,click,cpos,g_color in end_guide:
            if guide =="menu":
                screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
                screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

        boal.draw()
        pack1.draw()
        pack2.draw()

    #壁に当てちゃだめゲーム
    elif status ==38:
        screen.draw.text("壁にあてちゃダメゲーム", (220, 250), fontname="ipaexg.ttf", color="YELLOW", fontsize=32)
        screen.draw.text('Click:SPACE',(300,300),color = 'WHITE',gcolor = 'RED',fontsize=36)
    elif status == 39:
        screen.draw.text("UPキー：上へ", (50, 600), fontname="ipaexg.ttf", color="YELLOW", fontsize=32)
        screen.draw.text("DOWNキー：下へ", (100, 600), fontname="ipaexg.ttf", color="YELLOW", fontsize=32)
        for y in range(15):
                for x in range(20):
                    floorgi.topleft=(40*x,40*y)
                    floorgi.draw()
                    if map_giza[y][x] ==1:
                        boxgi.topleft=(40*x,40*y)
                        boxgi.draw()
                        boalgi.draw()
    elif status ==40:
        
        for y in range(15):
                for x in range(20):
                    floorgi.topleft=(40*x,40*y)
                    floorgi.draw()
                    if map_giza[y][x] ==1:
                        boxgi.topleft=(40*x,40*y)
                        boxgi.draw()
                        boalgi.draw()
        screen.draw.text("ダメ～", (220, 250), fontname="ipaexg.ttf", color="RED", fontsize=32)
                        
    elif status ==41:
        for y in range(15):
                for x in range(20):
                    floorgi.topleft=(40*x,40*y)
                    floorgi.draw()
                    if map_giza[y][x] ==1:
                        boxgi.topleft=(40*x,40*y)
                        boxgi.draw()
        screen.draw.text('goal',(160,200),color = 'WHITE',gcolor = 'BLUE',fontsize=72)

        
    
        

    if status ==3 or status == 4 or status == 7:
        shooter.draw()
        eship.draw()
    if status ==5 or status ==8:
        shooter.draw()
    if status ==6 or status == 9:
        eship.draw()
    if status >=10 and status <=19:
        for i in range(20):
            screen.draw.rect(star[i],'WHITE')

        for i in range(50):
            screen.draw.line((350-i*3,550+i),(450+i*3,550+i),'GRAY')
        rocket.draw()
        


def update():
    global eship_hp,turn,eshot,shooter_hp,status,i,j,k,l,a,b,c,d,enemy_hp,player_hp
    global speed,acceleration,key_flg,anime_r
    global turn1,turn2,bx,by,px,py,status,apoint,bpoint,Turn3
    
    for i in range(len(star)):
        star[i].y += i
        if star[i].y > HEIGHT:
            star[i].y =0
    if status ==4 :
        #自機のキー操作
        if keyboard.left:
            if shooter.x>47:
                shooter.x -= 3
        if keyboard.right:
            if shooter.x < WIDTH-47:
                shooter.x += 3
                
        #敵を左右に動かす
        if turn :
            eship.x += 5
            if eship.x > WIDTH:
                turn =False
        else:
            eship.x -= 5
            if eship.x <0:
                turn =True


        #敵のミサイルの角度        
        if eshot ==0:
            angle = eship.angle_to(shooter)
            missile1 = Actor('emissile.png',(eship.x-25,eship.y+10))
            missile2 = Actor('emissile.png',(eship.x+25,eship.y+10))
            missile3 = Actor('emissile.png',(eship.x+25,eship.y+10))
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
                    status=6
                e_missiles.remove(missile)
        #自機のミサイル
        for missile in s_missiles:
            missile.y -=10
            rect =Rect(missile.topleft,(16,22))
            if eship.colliderect(rect):
                eship_hp -= 1
                if eship_hp ==0:
                    status =5
                s_missiles.remove(missile)

    if status ==7:
        #自機のキー操作
        if keyboard.left:
            if shooter.x>47:
                shooter.x -= 3
        if keyboard.right:
            if shooter.x < WIDTH-47:
                shooter.x += 3
                
        #敵を左右に動かす
        if turn :
            eship.x += 10
            if eship.x > WIDTH:
                turn =False
        else:
            eship.x -= 10
            if eship.x <0:
                turn =True


        #敵のミサイルの角度        
        if eshot ==0:
            angle = eship.angle_to(shooter)
            missile1 = Actor('emissile.png',(eship.x-25,eship.y+10))
            missile2 = Actor('emissile.png',(eship.x+25,eship.y+10))
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
                    status=9
                e_missiles.remove(missile)
        #自機のミサイル
        for missile in s_missiles:
            missile.y -=10
            rect =Rect(missile.topleft,(16,22))
            if eship.colliderect(rect):
                eship_hp -= 1
                if eship_hp ==0:
                    status =8
                s_missiles.remove(missile)
    #STAGE 1
    if status ==11:
        if keyboard.up:
            key_flg =True
            acceleration =-0.1

        else:
            key_flg =False
            acceleration =0.1
        speed += acceleration
        rocket.y +=speed
        if rocket.y > 500:
            if speed<1.0:
                status =12
                
            else:
                status =13
                anime_r =animate(rocket, 'bounce_start_end',1,angle=45)
    #STAGE 2
    elif status ==14:
        if keyboard.up:
            key_flg =True
            acceleration =-0.2

        else:
            key_flg =False
            acceleration =0.2
        speed += acceleration
        rocket.y +=speed
        if rocket.y > 500:
            if speed<1.0:
                status =15
                
            else:
                status =16
                anime_r =animate(rocket, 'bounce_start_end',1,angle=45)
    #STAGE 3
    elif status ==17:
        if keyboard.up:
            key_flg =True
            acceleration =-0.3

        else:
            key_flg =False
            acceleration =0.3
        speed += acceleration
        rocket.y +=speed
        if rocket.y > 500:
            if speed<1.5:
                status =18
                
            else:
                status =19
                anime_r =animate(rocket, 'bounce_start_end',1,angle=45)

    #MAZE
    elif status ==21:
        def shou(a,b):
            for y in range(15):
                for x in range(20):
                    if map_data[y][x] !=0:
                        
                        if ((x*40 < a)
                        and (a<x*40+40) 
                        and (y*40<b) 
                        and (b< y*40+40)):
                            return 1;
        if a==1:
            for missile1 in p_missiles1:
                missile1.y -=10
                rect =Rect(missile1.topleft,(15,20))
                x=missile1.x
                y=missile1.y
                if shou(x,y)==1:
                    p_missiles1.remove(missile1)
                if enemy.colliderect(rect):
                    enemy_hp -= 1
                    p_missiles1.remove(missile1)
                    if enemy_hp ==0:
                        status=22
        if b==1:
            for missile2 in p_missiles2:
                missile2.y +=10
                rect =Rect(missile2.topleft,(15,20))
                x=missile2.x
                y=missile2.y
                if shou(x,y)==1:
                    p_missiles2.remove(missile2)
                elif enemy.colliderect(rect):
                    enemy_hp -= 1
                    p_missiles2.remove(missile2)
                    if enemy_hp ==0:
                        status=22
        if c==1:
            for missile3 in p_missiles3:
                missile3.x -=10
                rect =Rect(missile3.topleft,(15,20))
                x=missile3.x
                y=missile3.y
                if shou(x,y)==1:
                    p_missiles3.remove(missile3)
                elif enemy.colliderect(rect):
                    enemy_hp -= 1
                    p_missiles3.remove(missile3)
                    if enemy_hp ==0:
                        status=22
        if d==1:
            for missile4 in p_missiles4:
                missile4.x +=10
                rect =Rect(missile4.topleft,(15,20))
                x=missile4.x
                y=missile4.y
                if shou(x,y)==1:
                    p_missiles4.remove(missile4)
                elif enemy.colliderect(rect):
                    enemy_hp -= 1
                    p_missiles4.remove(missile4)
                    if enemy_hp ==0:
                        status=22
        if o==1:
            for missile5 in e_missiles1:
                missile5.y -=10
                rect =Rect(missile5.topleft,(15,20))
                x=missile5.x
                y=missile5.y
                if shou(x,y)==1:
                    e_missiles1.remove(missile5)
                elif player.colliderect(rect):
                    player_hp -= 1
                    e_missiles1.remove(missile5)
                    if player_hp ==0:
                        status=23
        if j==1:
            for missile6 in e_missiles2:
                missile6.y +=10
                rect =Rect(missile6.topleft,(15,20))
                x=missile6.x
                y=missile6.y
                if shou(x,y)==1:
                    e_missiles2.remove(missile6)
                elif player.colliderect(rect):
                    player_hp -= 1
                    e_missiles2.remove(missile6)
                    if player_hp ==0:
                        status=23
        if k==1:
            for missile7 in e_missiles3:
                missile7.x -=10
                rect =Rect(missile7.topleft,(15,20))
                x=missile7.x
                y=missile7.y
                if shou(x,y)==1:
                    e_missiles3.remove(missile7)
                elif player.colliderect(rect):
                    player_hp -= 1
                    e_missiles3.remove(missile7)
                    if player_hp ==0:
                        status=23
        if l==1:
            for missile8 in e_missiles4:
                missile8.x +=10
                rect =Rect(missile8.topleft,(15,20))
                x=missile8.x
                y=missile8.y
                if shou(x,y)==1:
                    e_missiles4.remove(missile8)
                elif player.colliderect(rect):
                    player_hp -= 1
                    e_missiles4.remove(missile8)
                    if player_hp ==0:
                        status=23
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
        def atari():
            global boalgi,status
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

        boalgi.x +=1
        if Turn3 :
            boalgi.y -=5
            atari()
        else:
            boalgi.y += 5
            atari()
        
        if keyboard.UP:
            Turn3 = True
        if keyboard.DOWN:
            Turn3 = False
    elif status ==40:
        if keyboard.SPACE:
            boalgi.center=(0,300)
            status=39

    
    

def on_key_down(key):
    global status,s_missiles,e_missiles,status,eship_hp,shooter_hp
    global speed,acceleration
    global a,b,c,d,o,j,k,l,player_hp,enemy_hp
    global location1,location2,player,enemy,p_missile,s_missile,shooter,eship,apoint,bpoint
    
    if key == keys.SPACE:
        if status ==1:
            status = 2
        
        elif status == 4 or status ==7 :
            s_missiles.append(Actor('smissile.png',shooter.pos))
        elif status ==20:
            player_hp=10
            enemy_hp=10
            s_missiles=[]
            e_missiles=[]
            location1 =[0,1]
            location2 =[13,18]
            player=Actor('player',topleft=(40,0))
            enemy=Actor('enemy',topleft=(720,520))
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
    if key == keys.RETURN:
        if status == 3 or status == 6:
                eship_hp =30
                shooter_hp=10
                s_missiles=[]
                e_missiles=[]
                status = 4
        elif status == 5 or status == 9:
                eship_hp =30
                shooter_hp=10
                s_missiles=[]
                e_missiles=[]
                status = 7
    
            
    
        
    if key == keys.SPACE and anime_r.running != True:
        #STAGE1
        if status == 10 or status == 13:
            
            status =11
            rocket.y=200
            speed =0
            acceleration =0.1
            rocket.angle =0
        #STAGE2    
        elif status == 12 or status ==16:
            status =14
            rocket.y=200
            speed =0
            acceleration =0.1
            rocket.angle =0
        #STAGE3    
        elif status == 15 or status == 19:
            status =17
            rocket.y=200
            speed =0
            acceleration =0.1
            rocket.angle =0

    #戻る
    if key == keys.P:
        if status ==2:
            status =1
        elif status ==3:
            shooter = Actor('shooter.png',(400,500))
            eship =Actor('eship.png',(400,100))
            status =2
        elif status ==5:
            shooter = Actor('shooter.png',(400,500))
            eship =Actor('eship.png',(400,100))
            status =2
        elif status ==6:
            shooter = Actor('shooter.png',(400,500))
            eship =Actor('eship.png',(400,100))
            status =2
        elif status ==8:
            shooter = Actor('shooter.png',(400,500))
            eship =Actor('eship.png',(400,100))
            status =2
        elif status ==9:
            shooter = Actor('shooter.png',(400,500))
            eship =Actor('eship.png',(400,100))
            status =2
        elif status ==10:
            status =2
        elif status ==11:
            status =2
        elif status ==12:
            status =2
        elif status ==13:
            status =2
        elif status ==14:
            status =2
        elif status ==15:
            status =2
        elif status ==16:
            status =2
        elif status ==17:
            status =2
        elif status ==18:
            status =2
        elif status ==19:
            status =2
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
            
    #SPACE SHOOTER オープニングへ
    if key == keys.A:
        if status ==2:
            status = 3
        if status == 21:
            #プレイヤーが端でなければ
            if location1[1] >= 1:
                if map_data[location1[0]][location1[1]-1] != 1:
                    location1[1] -= 1
                    player.x -=40
    #MOON LANDER　オープニングへ
    if key == keys.B:
        if status ==2:
            status = 10
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
        p_missiles1.append(Actor('pmissile1.png',player.pos))
        a=1

    if key == keys.G:
        p_missiles2.append(Actor('pmissile2.png',player.pos))
        b=1
    if key == keys.F:
        p_missiles3.append(Actor('pmissile3.png',player.pos))
        c=1
    if key == keys.H:
        p_missiles4.append(Actor('pmissile4.png',player.pos))
        d=1
    
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
        e_missiles1.append(Actor('emissile1.png',enemy.pos))
        o=1

    if key == keys.KP2:
        e_missiles2.append(Actor('emissile2.png',enemy.pos))
        j=1
    if key == keys.KP1:
        e_missiles3.append(Actor('emissile3.png',enemy.pos))
        k=1
    if key == keys.KP3:
        e_missiles4.append(Actor('emissile4.png',enemy.pos))
        l=1                              
    
        
            
            
            
        






                    

pgzrun.go()
