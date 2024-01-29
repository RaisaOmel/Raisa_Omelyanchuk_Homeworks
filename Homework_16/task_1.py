#Создайте класс Point3D, который хранит координаты x, y, z.
# Создайте статистический метод, который выведет результат x*y*z (где x = 2, y = 3, z = 4).
# Пропишите конструктор для создания экземпляров с локальными координатами.
# Также добавьте методы, позволяющие изменять координаты и получать их

class Point3D:
    def __init__(self,x ,y,z):
        self.__x=x
        self.__y=y
        self.__z=z

    @staticmethod
    def end(x,y,z):
        return x*y*z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self,x):
        self.__x=x

    @y.setter
    def y(self, y):
        self.__y = y

    @z.setter
    def z(self, z):
        self.__z = z

point=Point3D(1,2,3)
print(Point3D.end(2,3,4))
point.x=5
print(f'координаты {point.x},{point.y},{point.z}')

