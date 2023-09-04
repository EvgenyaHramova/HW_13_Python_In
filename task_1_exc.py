#  Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


class TriangleError(Exception):
    pass

class LineError(Exception):
    def __enter__(self, *args):
        self.args = Triangle()
        
    def __str__(self) -> str:
        
        return 'Длина стороны треугольника не может быть отрицательной или равной 0'
    



class Triangle:
    def __init__(self, a: float, b: float, c: float) -> None: # экземпляр класса
        self.a = a
        self.b = b
        self.c = c

    def validate(self):
        if (self.a or self.b or self.c) <= 0:
            raise LineError
        if (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            return self.isosceles() or self.versatile()
        else:
            raise TriangleError('Треугольника с такими сторонами не может быть!')
        
    
    def isosceles(self):
        if (self.a == self.b and self.b == self.c and self.c == self.a):
            return 'Треугольник является равносторонним'
        elif (self.a == self.b or self.a == self.c or self.b == self.c):
            return 'Треугольник является равнобедренным'
        
       
    # def isosceles(self):
    #     if (self.a == self.b or self.a == self.c or self.b == self.c):
    #         return 'Треугольник является равнобедренным'
        
    # def equilateral(self):
    #     if self.isosceles == True and (self.a == self.b and self.b == self.c and self.c == self.a):
    #         return 'Треугольник является равносторонним'        
    
    def versatile(self):
        if (self.a != self.b and self.b != self.c and self.c != self.a):
            return 'Треугольник - разносторонний'
    
    def __repr__(self):
        return f'a = {self.a}, b = {self.b}, c = {self.c}'

if __name__ == '__main__':    
    # abc = Triangle(int(input('Введите длину стороны A: ')), 
    #          int(input('Введите длину стороны B: ')), 
    #          int(input('Введите длину стороны C: ')))
    # print(abc.a, abc.b, abc.c)    

    t1 = Triangle(2,2,1)
    
    #print(t1.a, t1.b, t1.c)
    print(t1.validate())
    
    t2 = Triangle(5,5,5)
    print(t2.validate())
    
    t3 = Triangle(3,7,5)
    print(t3.validate())
    
    # t4 = Triangle(1,1,2)
    # print(t4.validate())
    t1 = Triangle(-2,2,1)
    #print(t1.a, t1.b, t1.c)
    print(t1.validate())