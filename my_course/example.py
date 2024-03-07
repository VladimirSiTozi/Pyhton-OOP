# class Car:
#     def __init__(self, brand: str, model: str):
#         self.brand = brand
#         self.model = model
#
# # List of Car objects
# cars = [
#     Car("Toyota", "Camry"),
#     Car("Honda", "Accord"),
#     Car("Ford", "Mustang"),
#     Car("Toyota", "Corolla"),
#     Car("Honda", "Civic"),
#     Car("Ford", "Fusion"),
# ]
#
# # Define a custom sorting key function
# def custom_sort(car):
#     return (car.brand, car.model)
#
# # Sort the list of cars using the custom sorting key
# sorted_cars = sorted(cars, key=custom_sort)
#
# # Print the sorted list of cars
# for car in sorted_cars:
#     print(f"Brand: {car.brand}, Model: {car.model}")


x = ['x', 's', 'y']
print(*x)