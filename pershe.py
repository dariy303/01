import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 200
        self.alive = True

    def to_study(self):
        print('Time to study!!!')
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 2

    def to_chill(self):
        print('I will chill')
        self.gladness += 3
        self.progress -= 0.1
        self.money -= 200

    def to_work(self):
        print('Time to work')
        self.gladness -= 1
        self.gladness -= 0.03
        self.money += 250
    def is_Alive(self):
        if self.progress < -0.5:
            print('Cast out')
            self.alive = False
        elif self.gladness <= 20:
            print('Depression')
            self.alive = False
        elif self.progress > 5:
            print('Passed extern')
            self.alive = False
        elif self.money <= -400:
            print('Банкрот')
            self.alive = False
        if self.money <= 0:
            self.to_work()
        if self.progress <= -0.25:
            self.to_study()
        if self.gladness <= 50:
            self.to_chill()
    def end_of_day(self):
        print(f'Gladness = {round(self.gladness, 0)}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f'Money = {self.money}')

    def live(self, day):
        day = "Day" + str(day) + ' of ' + self.name + ' life '
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_Alive()

ivan = Student(name='Ivan')

for day in range(366):
    if ivan.alive == False:
        break
    ivan.live(day)