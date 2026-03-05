from pgzero.actor import Actor
from .models import create_shooter, create_enemy
from .draw import opening_draw, battle_draw, game_clear_draw, game_over_draw
from .draw import game_start_guide, game_middle_guide, game_end_guide, game_over_guide
from .logic import move_shooter, move_enemy, enemy_missile_angle, enemy_missile, shooter_missile



class SpaceShooter:
    def __init__(self):
        self.status = 1
        self.turn = False
        self.eshot = 60
        self.shooter = create_shooter()
        self.enemy = create_enemy()



    def space_shooter_update(self, keyboard, WIDTH):
        #自機のキー操作
        move_shooter(self.shooter, keyboard, WIDTH)
        
        #敵を左右に動かす
        self.turn = move_enemy(self.status, self.enemy, self.turn, WIDTH)       


        #敵のミサイルの角度        
        if self.eshot == 0:
            enemy_missile_angle(self.enemy, self.shooter)
            self.eshot = 60 #時間をリセット 
        else:
            self.eshot -= 1
            

        #敵のミサイル
        self.status, self.shooter = enemy_missile(self.status, self.enemy, self.shooter)
            

        #自機のミサイル
        self.status, self.enemy = shooter_missile(self.status, self.enemy, self.shooter)

        return self



    def draw(self, screen):
        if self.status == 1:
            opening_draw(screen, self.shooter, self.enemy)
            
        elif self.status == 2 or self.status == 5:
            battle_draw(screen, self.status, self.shooter, self.enemy)

        elif self.status == 3 or self.status == 6:
            game_clear_draw(screen, self.status, self.shooter)

        elif self.status == 4 or self.status == 7:
            game_over_draw(screen, self.enemy)
            
        

    def update(self, keyboard, WIDTH):
        self.space_shooter_update(keyboard, WIDTH)
        

    def on_key_down(self, key):
        
        #ゲームスタート
        if key == key.RETURN:
            if self.status == 1 or self.status == 4:
                self.shooter = create_shooter()
                self.enemy = create_enemy()
                self.status = 2
            elif self.status == 3 or self.status == 7:
                self.shooter = create_shooter()
                self.enemy = create_enemy()
                self.status = 5

        #ミサイル発射
        if key == key.SPACE:
            if self.status ==2 or self.status == 5:
                self.shooter.missiles.append(Actor('smissile.png', self.shooter.actor.pos))
