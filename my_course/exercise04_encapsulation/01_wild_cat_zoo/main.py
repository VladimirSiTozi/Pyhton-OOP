from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker
from project.zoo import Zoo

a = Animal('cat', 'm', 1, 1)
print(a.__repr__())
l = Cheetah('Simba', 'm', 1, 1)
print(l.__repr__())
w = Worker("Pesho", 22, 2200)
print(w.__repr__())
k = Keeper("Pesho", 22, 2200)
print(w.__repr__())
zoo = Zoo('Zoo', 20000, 10, 10)
print(zoo.add_animal(l, 100))
print(zoo.hire_worker(k))
# print(zoo.fire_worker('Pesho'))
print(zoo.pay_workers())
print(zoo.tend_animals())