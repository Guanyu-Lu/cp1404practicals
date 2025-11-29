from prac_09.unreliable_car import UnreliableCar

my_car=UnreliableCar("My Car",100,30)
for i in range(100):#Conduct 100 tests
    print(f"Attempt {i+1:3}: Wanted to drive 10km, actually drove {my_car.drive(10):2}km")