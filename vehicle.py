from unicodedata import name


class Vehicle:
    color="White"
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    
    def congrats(self):
        
        return f"Hello  ,congratulations on getting you first {self.color} {self.name} that has a maximum speed of {self.max_speed}km/hr and a distance of {self.mileage} " 
    def space(self,capacity):
        return f"The {self.name} that has {capacity} seats "