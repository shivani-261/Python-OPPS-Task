class Point:

    def __init__(self,X,Y):
        print("init called")
        self.X=X
        self.Y=Y

    def __str__(self):
        print("str called")
        return "[{0},{1}]".format(self.X,self.Y)

    def __mul__(self,obj):
        print("mul called")
        X=self.X * obj.X
        Y=self.Y * obj.Y
        return Point(X,Y)


p1=Point(10,20)
print(p1)

p2=Point(30,40)
print("Multiplication of two obj is:",p1*p2)
print(p2)
