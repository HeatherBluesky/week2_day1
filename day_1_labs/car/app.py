class Engine:
    def __init__ (self, volume, horse_power):
        self.volume = volume 
        self.horse_power = horse_power


    def start(self):
        return "vroooom"

    def start(self):
        return "stopped"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model 
        self.engine = engine

    def drive(self):
        return self.engine.start()
    
    engine1 = Engine(6, 180)   #is an instance
    print(engine1.volume)
    print(engine1.start())


car1 = Car("Ford", "Mondeo", engine1)
print(car1.make)
print(car1.drive())