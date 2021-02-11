class Car:
    lokm=[]
    def __init__(self,name,velocity, time):
        self.name=name
        self.velocity=velocity
        self.time=time
    
    def calcDist(self):
        self.distance=self.time * self.velocity
        Car.lokm.append(self.distance)
        
        

car1=Car("ford",50,2)
car1.calcDist()
print(car1.distance)

car2=Car("peugeot",65,4)
car2.calcDist()
print(car2.distance)

car3=Car("tesla",75,3)
car3.calcDist()
print(car3.distance)


print(Car.lokm)