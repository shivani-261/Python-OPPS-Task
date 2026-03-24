class Box:
    def __init__(self,*args):
        if len(args)==0:
            self.width=1
            self.height=2
            self.depth=3
        elif len(args)==1:
            self.width=args[0]
            self.height=args[0]
            self.depth=args[0]
        elif len(args)==2:
            self.width=args[0]
            self.height=args[1]
            self.depth=args[1]
        elif len(args)==3:
            self.width=args[0]
            self.height=args[1]
            self.depth=args[2]
            
    def volume(self):
       print("volume of Box is:",self.width* self.height* self.depth)
r1=Box()
r2=Box(5)
r3=Box(4,6)
r4=Box(4,6,8)

r1.volume()
r2.volume()
r3.volume()
r4.volume()
    
