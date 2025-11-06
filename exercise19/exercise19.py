class Car:
    speed=""
    type=""
    color=""

    # def __init__(self):
    #     print('this will always be printed')
    # def __init__(self):
    #     self.speed='salma'
    # def __init__(self, car_type,car_speed):
    #     self.type = car_type
    #     self.speed = car_speed
    def drive(self):
        print(self.type+" is the car type")
    def properties(self,seats):
        print(self.color+" is the color and it has this number of seats: "+seats)    

ferrari=Car()
ferrari.speed="100"
# print(ferrari.speed)
ferrari.type="ferrari"
ferrari.color="pink"
ferrari.drive()
ferrari.properties('7')


bmw=Car()
bmw.speed="100"
bmw.type="bmw"
bmw.color="pink"

