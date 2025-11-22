from prac_09.silver_service_taxi import SilverServiceTaxi
print(SilverServiceTaxi("Hummer",100,4))
taxi=SilverServiceTaxi("SilverServiceTaxi", 100, 2)
taxi.drive(18)
current_fare = taxi.get_fare()
print(f"${current_fare:.2f}")
try:
    assert current_fare ==round(48.78,1) #Check whether the current_fare meets the expected value
    print("For an 18 km trip in a silver service taxi with fanciness of 2, the fare should is $48.80.")
except AssertionError:
    print("Wrong calculated fare")