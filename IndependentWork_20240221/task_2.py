#Gardener, TomatoBush, TomatoBush
#
class Gardener():
    def __init__(self, name):
        self.name=name
        self.__plant=[]

    def get_plant(self):
        return self.__plant

    def set_plant(self,bush_):
        self.__plant.append(bush_)

    def work(self):
        for bush_ in self.get_plant():
            bush_.grow_all()

    @staticmethod
    def knowledge_base(garder_):
        harvest = {}
        for bush_ in garder_.get_plant():
            rez = bush_.give_info()
            print(rez)
            # for key, val in rez.items():
            #     harvest[key] = harvest.get(key, 0) + val

        for key, val in harvest.items():
            print(f'{key} = {val}шт')
    def harvest(self):
        if len([1 for bush_ in self.__plant if not bush_.all_are_ripe()])==0:
            for bush_ in self.__plant:
                bush_.give_away_all()

            self.__plant = []
            print('урожай собрали')
        else:
            print('урожай еще не созрел')



class TomatoBush(Gardener):
    def __init__(self, garder_):
        self.tomato = []
        garder_.set_plant(self)

    def add_tomato(self, tomat):
        self.tomato.append(tomat)

    def grow_all(self):
        for tomat in self.tomato:
            tomat.grow()

    def all_are_ripe(self):
        return False if len([1 for elem in self.tomato if not elem.is_ripe()]) > 0 else True

    def give_info(self):
        harvest = {}
        #соберем инфо об урожае
        for tomat in self.tomato:
            val=tomat.states.get(tomat.get_state(),0)
            harvest[val] = harvest.get(val,0)+1
        return harvest
    def give_away_all(self):
        self.tomato = []

class Tomato(TomatoBush):
    states={0:"отсутствует", 1: 'Рассада', 2:"цветение", 3:"Зеленый", 4:"красный"}
    def __init__(self,bush,kol):
        self.__index = kol
        self.__state=0
        bush.add_tomato(self)

    def get_state(self):
        return self.__state
    def get_index(self):
        return self.__index

    def set_state(self,sum):
        self.__state+=sum
    def grow(self):
       if self.get_state() < 4:
          self.set_state(1)

    def is_ripe(self):
        return True if self.get_state() == 4 else False

#тесты
#п.2
garder=Gardener('Сад')
bush=TomatoBush(garder)
for elem in range(int(input('Введите кол-во помидор на кусту '))):
    tomato = Tomato(bush,elem+1)
#п.3
garder.work()
#п.4
garder.harvest()
#п.1
garder.knowledge_base(garder)
print('ухаживаем еще 3 раза')
#п.5
garder.work()
garder.work()
garder.work()
#п.1
garder.knowledge_base(garder)
#п.6
garder.harvest()