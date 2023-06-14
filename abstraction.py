class shape:
    def __init__(self,dil1,dil2):
        self.dil1=dil1
        self.dil2=dil2

    def area(self):
        print('shape has no area')

class trangle(shape):
    def area(self):
     area =0.5 * self.dil1 *self.dil2
     print("the traangle: ",area)

class recagle(shape):
   def area(self):
      area= self.dil1 *self.dil2
      print("rcetangle: ", area)

t1=trangle(23,12)
t1.area()
t2=recagle(12,4)
t2.area()