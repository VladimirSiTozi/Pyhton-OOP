from project.horse_race_app import HorseRaceApp
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred

horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 120))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 139))

# horse1 = Appaloosa("Spirit", 111)
# print(horse1)
# horse1.train()
# print(horse1.speed)
# horse1.train()
# print(horse1.speed)

horse2 = Thoroughbred("Rocket", 136)
print(horse2)
horse2.train()
print(horse2.speed)
horse2.train()
print(horse2.speed)