#1.	Требуется проверить, возможно ли из представленных отрезков условной длины  сформировать треугольник.
# Для этого создайте класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
#•	Ура, можно построить треугольник!
#•	С отрицательными числами ничего не выйдет!
#•	Жаль, но из этого треугольник не сделать.
class TriangleChecker():
   @staticmethod
   def is_triangle(a=0,b=0,c=0):
        print(f'Длины:1 отрезка={a}, 2 отрезка={b}, 3 отрезка={c}')
        if a<0 or b<0 or c<0:
           print("С отрицательными числами ничего не выйдет!")
        elif a==0 or b==0 or c==0:
            print("Жаль, но из этого треугольник не сделать")
        elif -1 <(a**2+b**2-c**2)-2*a*b < 1:
            print("Ура, можно построить треугольник!")
        else:
            print("Жаль, но из этого треугольник не сделать")

TriangleChecker.is_triangle(*[int(input('введите длину '+str(elem+1)+' отрезка ')) for elem in range(3)])



