from random import randint
import time

print("Welcome to the Airplane Simulator!")
time.sleep(1)
print("You are the pilot of a plane and you have to land it safely.")
time.sleep(1)

def create_pilot():
    skill = randint(0, 6)
    luck = randint(-5, 10) + skill
    pilot = [
    {"name": "", "experience": 0, "skill": skill, "luck": luck}
    ]
    pilot[0]["name"] = input("Enter your name:")
    print("Creating pilot...")
    time.sleep(2)
    print("Pilot created!")
    time.sleep(0.5)
    print("Pilot name:", pilot[0])

create_pilot()

def chose_plane():
    airplanes = [
        {"name": "Boeing 747", "class": "Commercial Airline", "takeoff": -5, "flying": 2, "landing": -2},
        {"name": "F-22 Raptor", "class": "Fighter Jet", "takeoff": -10, "flying": -10, "landing": -20},
        {"name": "Cessna 172", "class": "General Aviation", "takeoff": 5, "flying": 5, "landing": 3},
        {"name": "C-130 Hercules", "class": "Cargo Plane", "takeoff": 0, "flying": 1, "landing": -10},
        {"name": "Gulfstream G650", "class": "Business Jet", "takeoff": 1, "flying": 3, "landing": 2},
        {"name": "x-15", "class": "Experimental", "takeoff": -30, "flying": -25, "landing": -20},
        {"name": "SR-71 Blackbird", "class": "Spy Plane", "takeoff": -15, "flying": -20, "landing": -15}
    ]
    print("Welcome to the hangar!")
    time.sleep(0.5)
    for indice, plane in enumerate(airplanes):
        print(f"{plane["name"]} - {plane["class"]} - code -> {indice}")
        
    chose = int(input("Choose your plane by code:"))
    planeselected = airplanes[chose]
    print(f'You chose the {planeselected["name"]}')

chose_plane()