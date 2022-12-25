class Engine:

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __str__(self):
        return f"{self.power} {self.company}"


class Person:

    def __init__(self, age: int, fullname: str):
        self.__age = age
        self.fullName = fullname

    def __str__(self):
        return f"{self.fullName}"


class Driver(Person):

    def __int__(self, experience: int):
        self.experience = experience

    def __str__(self):
        return f"{self.experience}"


class Car:

    def __init__(self, carclass: str, engine: Engine, driver: Driver, marka: str):
        self.carClass = carclass
        self.engine = engine
        self.driver = driver
        self.marka = marka

    @staticmethod
    def start():
        print("Poexali")

    @staticmethod
    def stop():
        print("Ostanavlivaemsa")

    @staticmethod
    def turnRight():
        print("Povorot Napravo")

    @staticmethod
    def turnLeft():
        print("Povorot Nalevo")

    def __str__(self):
        return f"{self.driver}"


class Lorry(Car):

    def __init__(self, carrying: int, carclass: str, engine: Engine, driver: Driver, marka: str):
        super().__init__(carclass, engine, driver, marka)
        self.carying = carrying

    def __str__(self):
        return self.carying


class SportCar(Car):

    def __init__(self, speed: int, carclass: str, engine: Engine, driver: Driver, marka: str):
        super().__init__(carclass, engine, driver, marka)
        self.speed = speed

    def __str__(self):
        return f"{self.speed}"


e = Engine(500, "KzAuto")
d = Driver(12, "FS")
c = Car("sport", e, d, "Honda")
s = SportCar(1000, "Subaru", e, d, "Forester")
print(s.marka)
print(c.marka)
s.turnRight()
print(s)


