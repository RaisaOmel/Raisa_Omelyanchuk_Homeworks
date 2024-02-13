class My_class:
    def metod_new(self):
        global my_id
        my_id += 1
        self.id = my_id

class Vehicle(My_class):
    pass


class Tankman(My_class):
    pass


class Tank(Vehicle):
    def __init__(self):
        object_id_collector = self.id


class TankCommander(Tankman):
    def __init__(self):
        object_id_collector = self.id


class TankGunner(Tankman):
    def __init__(self):
        object_id_collector = self.id


def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (TankGunner().id, TankGunner().id, Tank().id, TankCommander().id, Tank().id)
    assert actual_ids == expected_ids, 'Expected_ids: {}. Actual_ids: {}.'.format(expected_ids, actual_ids)
    print('Test passed. Amazing job!')


my_id=0
def my_metod():

    TankGunner.__init__=TankGunner.metod_new
    Tank.__init__=Tank.metod_new
    TankCommander.__init__=TankCommander.metod_new

my_metod()
try:
    check_object_id_collector()
except AssertionError as string:
    print(string)