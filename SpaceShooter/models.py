from dataclasses import dataclass
from pgzero.actor import Actor

#SPACE SHOOTER　宣言
@dataclass
class EnemyRecord:
    actor: object
    hp: int
    missiles:list

def create_shooter():
    return EnemyRecord(
    actor=Actor('shooter.png',(400,500)),
    hp=10,
    missiles=[]
)

def create_enemy():
    return EnemyRecord(
    actor=Actor('eship.png',(400,100)),
    hp=1,
    missiles=[]
)
