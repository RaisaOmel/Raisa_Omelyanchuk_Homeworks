#И2.	Создайте суперкласс «Персональные компьютеры» и на его основе подклассы:«Настольные ПК» и «Ноутбуки».
# В классе-родителе определите общие свойства: размер памяти, модель. А в классах-потомках уникальные свойства:
#- для настольных: монитор, клавиатура, мышь; и метод для вывода этой информации
#- для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации.

class Computer():
    def __init__(self,memory,model):
        self.model=model
        self.memory=memory

class Laptop(Computer):
    def __init__(self,memory,model,heigth,width,diagoal):
        super().__init__(memory,model)
        self.heigth = heigth
        self.width = width
        self.diagoal = diagoal

    def __str__(self):
        return f'Laptop: model={self.model}, memory={self.memory} heigth={self.heigth}, width={self.width}, diagoal={self.diagoal}'

class DesktopPC(Computer):
    def __init__(self,memory,model,monitor,keyboard,mouse):
        super().__init__(memory,model)
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __str__(self):
        return f'DesktopPC: model={self.model}, memory={self.memory} monitor={self.monitor}, keyboard={self.keyboard}, mouse={self.mouse}'


laptop=Laptop(102,"PC",20,370,40)
print(laptop)
desktop=DesktopPC(1024,'Linux','Philips','Genius','smarbuy')
print(desktop)
