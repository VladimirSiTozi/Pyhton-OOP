from project.car import Car


class SportsCar(Car):
    def race(self):
        return 'racing...'


#  Test Code:
# sc = SportsCar()
# print(sc.move())
# print(sc.drive())
# print(sc.race())
