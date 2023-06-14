class student:
    roll=''
    gpa=''

    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa


    def display(self):

         print (f'this roll: {self.roll} he Gpa: {self.gpa}')


rahim =student(234,4.56)

rahim.display()
'''rahim=student()
rahim.roll=101
rahim.gpa=3.80
rahim.display()'''


'''rahim=student()
#print(isinstance(rahim,student))
rahim.roll=101
rahim.gpa=3.80'''
