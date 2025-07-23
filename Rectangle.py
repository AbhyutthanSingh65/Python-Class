class rect:
    def set_dim(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
n=[]
d=int(input("enter no of rectangles:"))
for i in range(d):
    R=rect()
    a=int(input("enter lentgh of rectangle:"))
    b=int(input("enter breadth of rectangle:"))
    R.set_dim(a,b)
    n.append(R)
index=1
for i in n:
    print("AREA OF RECTANGLE {} : {}".format(index,i.area()))
    index+=1
