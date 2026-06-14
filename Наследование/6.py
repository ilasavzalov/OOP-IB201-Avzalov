class Transport:
    pass

class WaterTransport(Transport):
    pass

class SurfaceWaterTransport(WaterTransport):
    pass

class SubmarineWaterTransport(WaterTransport):
    pass

class Ship(SurfaceWaterTransport):
    pass

class Boat(SurfaceWaterTransport):
    pass

class NuclearSubmarine(SubmarineWaterTransport):
    pass

class DieselSubmarine(SubmarineWaterTransport):
    pass

class AirTransport(Transport):
    pass

class Aviation(AirTransport):
    pass

class PistonAviation(Aviation):
    pass

class JetAviation(Aviation):
    pass

class Helicopter(Aviation):
    pass

class Aerostation(AirTransport):
    pass

class GroundTransport(Transport):
    pass

class RailwayTransport(GroundTransport):
    pass

class AutomobileTransport(GroundTransport):
    pass

class Car(AutomobileTransport):
    pass

class Truck(AutomobileTransport):
    pass

class Bus(AutomobileTransport):
    pass

class BicycleTransport(GroundTransport):
    pass

class AnimalDrivenTransport(GroundTransport):
    pass

class SpaceTransport(Transport):
    pass

class Rocket(SpaceTransport):
    pass

