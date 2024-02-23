# 8
"""Создайте класс Робот
создайте 2 типа оружия: меч, автомат
Создайте 2 типа амуниции: броня, шлем
Добавьте оружию и амуниции свои характеристики(например урон, прочность)
Создайте своего робота с каким либо оружием
(может быть несколько и брони может быть несколько. Также может быть ничего)
Выведите весь арсенал робота на экран
"""

class Robot:
    def __init__(self,name):
        self.name=name
        self.weapon={}
        self.ammunition={}

    def get_weapon(self,weapon_):
        self.weapon[weapon_.name]={'uron':weapon_.uron, 'strength':weapon_.strength}

    def get_ammunition(self,ammunition_):
        self.ammunition[ammunition_.name]={'uron':ammunition_.uron, 'strength':ammunition_.strength}

    def info(self):
        print(f'робот {self.name} имеет:')
        for key,val in self.ammunition.items():
             print(f"{key}: урон={val['uron']}, прочность={val['strength']}")
        for key,val in self.weapon.items():
            print(f"{key}: урон={val['uron']}, прочность={val['strength']}")
class Weapon:
    def __init__(self,name,uron,strength):
        self.name=name
        self.uron=uron
        self.strength=strength

    def get_weapon(self,robot):
        robot.weapon[self.name]={'uron':self.uron, 'strength':self.strength}
class Ammunition:
    def __init__(self,name,uron,strength):
        self.name=name
        self.uron=uron
        self.strength=strength

    def get_ammunition(self, robot):
        robot.weapon[self.name] = {'uron': self.uron, 'strength': self.strength}


ammunition=Ammunition('броня',0,50)
ammunition2=Ammunition('шлем',0,40)

weapon=Weapon('меч',10,30)
weapon2=Weapon('автомат',100,90)

robot=Robot('Друид')
ammunition.get_ammunition(robot)
weapon.get_weapon(robot)
robot.get_ammunition(ammunition2)
robot.get_weapon(weapon2)
robot.info()