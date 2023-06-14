#prant class,super class,base calsss
#child class,sub class,derived class

'''class phone:
     def call(self):
          print('can you ar call')

     def massage(self):
          print("you no tumi amka valobaso nha")


class redmi(phone):
     
     def camra(self):
          print('i no amar camara onek better')


s1=redmi()
s1.call()
s1.camra
s1.massage()'''

#overriding:
class phone:
    def __init__(self) -> None:
        print("I am phone class")

class redmi(phone):
    def __init__(self) -> None:
        #super().__init__()
        print("ami kew ke valobasi na ")
s2=redmi()

