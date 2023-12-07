class Sports:
    def __init__(self, name):
        self.name = name
    

    @property
    def sports_name(self):
        return self.name

    def practice(self):
        print("Doing Sports practice")


    @sports_name.setter
    def sports_name(self, value):
        self._name = value


class LandSports(Sports):
    def __init__(self, name, field):
        super().__init__(name)
        self._field = field


    @property
    def landsports_field(self):
        return self._field

    def practice(self):
        print("Doing LandSports practice")


class WaterSports(Sports):
    def __init__(self, name, activity):
        super().__init__(name)
        self._activity =  activity


    @property
    def watersports_field(self):
        return self._activity

    def practice(self):
        print("Doing WaterSports practice")

#Example of usage
if __name__ == "__main__":
    # Creating a new LandSports object
    baseball = LandSports("baseball", "baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    baseball.practice()

    water_skiing = WaterSports("Water Sliing", "Strap on your skiing and")
    print(water_skiing.sports_name)
    print(water_skiing.watersports_field)
    water_skiing.practice()

    sports = Sports("Softball")
    print(sports.sports_name)
    sports.practice()