# number of cars
cars = 100
# how many passengers can in each car
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of empty cars which have not drivers
cars_not_driven = cars - drivers
# number of cars which can run because they have drivers
cars_driven = drivers
# today's all passengers number
carpool_capacity = cars_driven * space_in_a_car
# how many passengers in each car today
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
