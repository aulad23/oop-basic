class Trangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

        
    def cul_culator(self):
        area = 0.5 *self.base *self.height
        print(area)
t1=Trangle(23,22)
t1.cul_culator()