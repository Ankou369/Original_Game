from pgzero.actor import Actor

moon_lander = Actor('rhome', center = (620, 200))
space_shooter = Actor('shome', center=(185, 200))
no_touch_game = Actor('ghome', center=(400, 200))
shooting_surival = Actor('hhome', center=(185, 450))
air_hockey_1 = Actor('bhome1', center=(670, 450))
air_hockey_2 = Actor('bhome2', center=(570, 450))
air_hockey_3 = Actor('bhome3', center=(620, 450))

def opening_draw(screen):
    screen.draw.text('S P A C E  G A M E S',(160,290),color = 'WHITE',gcolor = 'YELLOW',fontsize=72)
    screen.draw.text('click SPACE',(335,400),color = 'WHITE',gcolor = 'RED',fontsize=30)

def menu_draw(screen):
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
