from random import randint
import time

print("Welcome to the Airplane Simulator!")
time.sleep(1)
print("You are the pilot of a plane and you have to land it safely.")
time.sleep(1)

def create_pilot():
    skill = float(randint(0, 6))
    luck = float(randint(-5, 10) + skill)
    pilot = [
    {"name": "", "experience": 0, "skill": skill, "luck": luck}
    ]
    pilot[0]["name"] = input("Enter your name:")
    print("Creating pilot...")
    time.sleep(2)
    print("Pilot created!")
    time.sleep(1.5)
    print("Pilot name:", pilot[0])
    time.sleep(4.5)
    return pilot[0]

you_pilot = create_pilot()

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
    time.sleep(1.5)
    for indice, plane in enumerate(airplanes):
        print(f"{plane["name"]} - {plane["class"]} - code -> {indice}")
        
    chose = int(input("Choose your plane by code:"))
    planeselected = airplanes[chose]
    time.sleep(1.3)
    print(f'You chose the {planeselected["name"]}, is a {planeselected["class"]}!')
    time.sleep(5)
    return planeselected


your_planeselected = chose_plane()

class fly:
    def __init__(self, pilot, planeselected, point=0, chance=3):
        self.pilot = pilot
        self.planeselected = planeselected
        self.point = point
        self.chance = chance
    
    def tekeoff(self):
        climate = randint(-5, 5) + self.pilot["luck"]
        if climate > 5:
            print("Winds are favorable for takeoff!")
            time.sleep(2.5)
        test = self.pilot["skill"] + self.planeselected["takeoff"] + climate + self.pilot["experience"]
        print(f'Teste:{test}')
        if test >= 3 and test <= 7:
            print("Good takeoff!")
            self.point += test
            time.sleep(2.5)
        elif test > 7:
            print("Smooth takeoof!")
            self.point += test
            time.sleep(2.5)
        elif test < 3 and test >= 0:
            print("Takeoff was uneventful!")
            self.point += test
            time.sleep(2.5)
        else:
            print("Bad tekeoff!")
            live_or_die = randint(-10, 1) + self.pilot["luck"]
            print("live_or_die:", live_or_die)
            if live_or_die > 0:
                second_chance = input("Do you want to try again? (yes or no)")
                while second_chance == "yes" and self.chance >= 1:
                    self.tekeoff()                                
                print("You crashed!")
                exit()
            else:               
                print("You crashed!")
                exit()

    def flying(self):
        print("Flying...")
        time.sleep(3)

        climate = randint(-4, 3) + self.pilot["luck"]
        if climate >= 3:
            print("Good weather en route!!")
            time.sleep(3)
        elif climate < 3 and climate > 0:
            print("Winds are calm!")
            time.sleep(3)
        elif climate == -1:
            print("Turbulence!")
            time.sleep(3)
        elif climate == -2:
            print("Crosswind!")
            time.sleep(3)
        elif climate < -2:
            print("Storm!")
            time.sleep(3)
        test = self.pilot["skill"] + self.planeselected["flying"] + climate + self.pilot["experience"]
        if test >= 3 and test <= 7:
            print("Good flight!")
            self.point += test
            time.sleep(2.5)
        elif test > 7:
            print("Smooth flight!")
            self.point += test
            time.sleep(2.5)
        elif test < 3 and test >= 0:
            print("Flight was uneventful!")
            self.point += test
            time.sleep(2.5)
        else:
            print("Bad flight!")
            live_or_die = randint(-10, 1) + self.pilot["luck"]
            if live_or_die > 0:
                second_chance = input("Do you want to try again? (yes or no)")
                while second_chance == "yes" and self.chance >=1:
                    self.flying()                
                print("You crashed!")
                exit()
            else:               
                print("You crashed!")
                exit()
        time.sleep(4)

    def landing(self):
        print("You are approaching the airport...")
        time.sleep(3.5)
        print("Prepare for landing...")
        time.sleep(2.7)
        tower_control = randint(-5, 5) + self.pilot["luck"]
        while tower_control <= 0:
            print("Tower control: - Go around!")
            tower_control += 1
            time.sleep(3)
        print("The tower clared you for landing!")
        time.sleep(3)
        climate = randint(-4, 2) + self.pilot["luck"]
        test = self.pilot["skill"] + self.planeselected["landing"] + climate + self.pilot["experience"]
        if test >= 20:
            print("GREASER!!")
            self.point += test
            time.sleep(3.5)
            print("The flying was perfect!")
            self.pilot["skill"] += self.point
            self.pilot["experience"] += 1
            time.sleep(2.5)
            print("You completed the flight!")
        elif test >= 0 and test < 20:
            print("Good Landing!")
            self.point += test
            self.pilot["skill"] += self.point
            self.pilot["experience"] += 1
            time.sleep(3.5)
            print("You completed the flight!")
        else:
            print("Bad Landing!")
            time.sleep(2.5)
            print("You not complet the flight!")

voo = fly(you_pilot, your_planeselected)

voo.tekeoff()
voo.flying()
voo.landing()