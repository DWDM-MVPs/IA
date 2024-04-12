car = {
    "brand": "toyota",
    "color": "black",
    "plate": "11-TT-23"
}
print(car["brand"])

car["color"] = "blue"
print(car)

car["plate"] = "33-ZU-23"
print(car)

car["year"] = 2010
print(car)

for my_car in car.items():
    print(my_car)

for my_key, my_value in car.items():
    print("Key: {}\tValue: {}".format(my_key, my_value))

print("model" not in car.keys())