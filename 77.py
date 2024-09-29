import random
class Human:
    def __init__(self, name="Human", job = None, home = None, car = None,):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.hungry = 0
        self.job = job
        self.car = car
    def get_home(self, house = None):
        self.home = house()

    def get_car(self, brand=None):
        self.car = Auto(brand)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=8:
            self.shopping("food")
        else:
            if self.hungry<=10:
                self.hungry=10
                return
            self.hungry -=10
            self.home.food -=10

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<=20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness
            self.hungry += 5
    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<=20:
                manage ="fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Buying fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Buying food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicious":
            print("Buying delicious")
            self.money -= 15
            self.gladness += 10
            self.hungry -=2
    def chill(self):
        self.gladness += 10
        self.home.mess +=5

    def clean(self):
         self.home.mess -= 100
         self.gladness -=5
         self.hungry +=2
    def days(self, day):
        day = f"Today is {day} day of {self.name}"
        print(f"{day:=^50}", "\n")
        human_stats = self.name + "indexes"
        print(f"{human_stats :=^50}", "\n")
        print(f"Money{self.money}")
        print(f"Hungry{self.hungry}")
        print(f"Gladness{self.gladness}")
        home_stats = "Home indexes"
        print(f"Food{self.home.food}")
        print(f"Mess{self.home.mess}")
        print(f"{human_stats :=^50}", "\n")
        car_stats = f"{self.car.brand} car indexes"
        print(f"{car_stats:=^50}", "\n")
        print(f"Fuel{self.Fuel}")
    def is_alive(self):
        if self.gladness <=0:
            print("You jump under car")
            return False
        if self.hungry >=100:
            print("You starved to death")
            return False
        if self.money <-500:
            print("You have no money, you are lox")
            return False

    def live(self, day):
       if self.is_alive() == False:
           return False
       if self.home is None:
           print("You are lox")
       if self.job is None:
           self.get_job()
           print("You are lox")
           self.days(day)
           dice = random.randint(1,4)
       if self.hungry >20:
           print("Go eat")
           self.eat()
       if self.gladness <20:
            if self.home.mess > 15:
                print("I want sleep, but i have to clean home")
                self.clean()
            else:
                print("Now I can sleep")
                self.chill()
       elif self.money <0:
           print("I`m must work")
           self.work()
       elif dice == 1:
           print("Let`s chill")
           self.chill()
       elif dice == 2:
           print("I must work")
           self.work()
       elif dice == 3:
           print("I must clean home")
           self.clean()
       elif dice == 4:
           print("Cake time")
           self.shopping(manage = "delicious")

    def to_repair(self):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption =brand_list[self.brand]["consumption"]

    def drive(self):
        if self.fuel >= self.consumption:
            self.fuel -= self.consumption
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
"Java developer":
{"salary":50, "gladness_less": 10 },
"Python developer":
{"salary":40, "gladness_less": 3 },
"C++ developer":
{"salary":45, "gladness_less": 25 },
"Rust developer":
{"salary":70, "gladness_less": 1 },
}
brands_of_car = {
"BMW":{"fuel":100, "strength":100,
"consumption": 6},
"Lada":{"fuel":50, "strength":40,
"consumption": 10},
"Volvo":{"fuel":70, "strength":150,
"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,
"consumption": 14},
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

Maksim = Human(name="Maksim")
for day in range(1,8):
    if Maksim.live(day) == False:
        break










