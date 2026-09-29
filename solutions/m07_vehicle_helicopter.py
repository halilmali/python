"""
Module 7 worked example — Jun 2023 P41 Q2 (32 marks): parent class Vehicle
(speed logic with a max-speed limit), child class Helicopter adding vertical
movement and overriding IncreaseSpeed(); an output procedure that prints
vertical data only when the object is a helicopter; main instantiates a car and
a helicopter and increases each one's speed twice.

Run:  python m07_vehicle_helicopter.py
"""

class Vehicle:
    # self.__VehicleID        : STRING
    # self.__MaxSpeed         : INTEGER
    # self.__CurrentSpeed     : INTEGER
    # self.__IncreaseAmount   : INTEGER
    # self.__HorizontalPosition : INTEGER
    def __init__(self, vehicle_id, max_speed, increase_amount):
        self.__VehicleID = vehicle_id
        self.__MaxSpeed = max_speed
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = increase_amount
        self.__HorizontalPosition = 0

    def GetVehicleID(self):
        return self.__VehicleID

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetIncreaseAmount(self, amount):
        self.__IncreaseAmount = amount

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed * 2   # per the spec


class Helicopter(Vehicle):
    # self.__VerticalPosition : INTEGER
    # self.__VerticalChange   : INTEGER
    # self.__MaxHeight        : INTEGER
    def __init__(self, vehicle_id, max_speed, increase_amount,
                 vertical_position, vertical_change, max_height):
        super().__init__(vehicle_id, max_speed, increase_amount)
        self.__VerticalPosition = vertical_position
        self.__VerticalChange = vertical_change
        self.__MaxHeight = max_height

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):                    # overrides the parent method
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        Vehicle.IncreaseSpeed(self)             # horizontal logic from the parent


def Output(VehicleToOutput):
    print("ID:", VehicleToOutput.GetVehicleID(),
          "Speed:", VehicleToOutput.GetCurrentSpeed(),
          "Position:", VehicleToOutput.GetHorizontalPosition())
    if isinstance(VehicleToOutput, Helicopter):       # type-dependent output
        print("  Height:", VehicleToOutput.GetVerticalPosition())


def main():
    car = Vehicle("Tiger", 120, 30)
    helicopter = Helicopter("Lion", 100, 20, 0, 5, 50)
    car.IncreaseSpeed()
    car.IncreaseSpeed()
    helicopter.IncreaseSpeed()
    helicopter.IncreaseSpeed()
    Output(car)
    Output(helicopter)


main()
