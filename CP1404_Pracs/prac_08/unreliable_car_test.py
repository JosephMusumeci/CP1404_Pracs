"""
Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar

def main():
    dodgy_car = UnreliableCar("Dodgy Car", 100, 50)

    for i in range (1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km" .format(dodgy_car.name, dodgy_car.drive(i)))

    print(dodgy_car)

main()
