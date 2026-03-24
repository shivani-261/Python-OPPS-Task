class point:

    def __init__(self,X,Y):
        print("init called")
        self.X=X
        self.Y=Y
    def __str__(self):
        print("str called")
        return "({0},{1})".format (self.X,self.Y)
    def __add__(self,obj):
        print("add called")
        X=self.X+obj.X
        Y=self.Y+obj.Y
        return point(X,Y)
p1=point(10,20)
print(p1)
p2=point(30,40)
print(p2)
print("Addition of 2 objects is:",p1+p2)

