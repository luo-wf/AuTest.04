
class Game:
    def __init__(self, my_hp,enemy_hp,my_power, enemy_power):
        self.my_hp = my_hp
        self.my_power =  my_power
        self.enemy_hp =  enemy_hp
        self.enemy_power =  enemy_power

    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            print(self.enemy_hp)

            if self.my_hp > self.enemy_hp:
                print("我赢了")
                break
            else:
                print("敌人赢了")
                break


class HouYi(Game):
    def __init__(self, my_hp, enemy_hp, my_power, enemy_power):
        self.defense = 100
        super().__init__(my_hp, enemy_hp, my_power, enemy_power)

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            print(self.enemy_hp)

            if self.my_hp > self.enemy_hp:
                print("我赢了")
                break
            else:
                print("敌人赢了")
                break


houyi=HouYi(1300,1000,200,100)
houyi.fight()
#game1=Game()
#game1.fight()