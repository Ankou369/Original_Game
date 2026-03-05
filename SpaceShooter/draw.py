#####　ガイドテキスト　############################################################################
def game_start_guide(screen):
    #初めのガイド
    start_guide = [("start",(550,150),"click Enter",(650,150),'RED'),
                   ("back" ,(550,100),"click P"    ,(650,100),'YELLOW')]
    #初めのガイド
    for guide,gpos,click,cpos,g_color in start_guide:
        screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

def game_middle_guide(screen):
    #ゲームクリア時のガイド
    end_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                 ("next", (550, 150), "click Enter", (650, 150), 'RED'   )]
    
    #ゲームクリア時のガイド
    for guide,gpos,click,cpos,g_color in end_guide:
        screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

def game_end_guide(screen):
    #ゲームクリア時のガイド
    end_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                 ("next", (550, 150), "click Enter", (650, 150), 'RED'   )]
    
    #終わりのガイド
    for guide,gpos,click,cpos,g_color in end_guide:
        if guide =="menu":
            screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
            screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)

def game_over_guide(screen):
    #ゲームオーバー時のガイド
    game_over_guide = [("menu", (550, 100), "click P"    , (650, 100), 'YELLOW'),
                       ("restart", (550, 150), "click Enter", (650, 150), 'RED'   )]
    
    #ゲームオーバー時のガイド
    for guide,gpos,click,cpos,g_color in game_over_guide:
        screen.draw.text(guide, gpos, color = 'WHITE', gcolor = g_color, fontsize=30)
        screen.draw.text(click, cpos, color = 'WHITE', gcolor = g_color, fontsize=30)
#################################################################################

def opening_draw(screen,shooter, enemy):
    screen.draw.text('S P A C E  S H O O T E R',(120,290),color='WHITE',gcolor = 'YELLOW',fontsize =72)
    game_start_guide(screen)

    shooter.actor.draw()
    enemy.actor.draw()


def battle_draw(screen,status, enemy, shooter):
    #SPACE SHOOTER HPの描写
    hp = [(f'Enemy HP = {enemy.hp}'    , (50 ,50)),
          (f'Shooter HP = {shooter.hp}', (600,50))]
    
    now_stage = (status + 1) // 3 # 2,3,4ならSTAGE１,5,6,7ならSTAGE2
    
    screen.draw.text(f'STAGE {now_stage}',(300,300),color ='YELLOW',fontsize =64)

    #ミサイルの描写
    for missile in shooter.missiles:
        missile.draw()
    for missile in enemy.missiles:
        missile.draw()
    #HPの描写
    for text,pos in hp:
        screen.draw.text(text,pos,color='YELLOW',fontsize = 32)

    shooter.actor.draw()
    enemy.actor.draw()
    
            
def game_clear_draw(screen,status,shooter):
    now_stage = (status + 1) // 3 # 4,5ならSTAGE１,７,8ならSTAGE2
    
    screen.draw.text('G A M E  C L E A R',(310,290),color ='WHITE',gcolor ='YELLOW',fontsize=32)
    shooter.actor.draw()
    
    if now_stage == 1:
        game_middle_guide(screen)
    else:
        game_end_guide(screen)

def game_over_draw(screen,enemy):
    screen.draw.text('G A M E  O V E R',(310,290),color ='WHITE',gcolor ='RED',fontsize=32)
    enemy.actor.draw()
    
    game_over_guide(screen)
    
