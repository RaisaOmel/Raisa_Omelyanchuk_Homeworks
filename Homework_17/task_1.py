#Создайте класс Vector, представляющий вектор в трехмерном пространстве.
# Определите магические методы для арифметических операторов (+, -, *, /),
# чтобы можно было выполнять операции над векторами.
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __mul__(self, other):
        return Vector(self.x*other.x,self.y*other.y,self.z*other.z)

    def __truediv__(self, other):
        return Vector(round(self.x/other.x,2),round(self.y/other.y,2),round(self.z/other.z,2))

vect1=Vector(10,4,15)
print(f'№1 {vect1.x} {vect1.y} {vect1.z}')
vect2=Vector(2,1,3)
print(f'№2 {vect2.x} {vect2.y} {vect2.z}')
vect3=vect1+vect2
print(f'сложение {vect3.x} {vect3.y} {vect3.z}')

vect3=vect1-vect2
print(f'вычетание {vect3.x} {vect3.y} {vect3.z}')

vect3=vect1*vect2
print(f'умножение {vect3.x} {vect3.y} {vect3.z}')

vect3=vect1/vect2
print(f'деление {vect3.x} {vect3.y} {vect3.z}')


