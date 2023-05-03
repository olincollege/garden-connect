"""jhgfj"""
from datetime import datetime
from weather_derivation import weather_data
from plant_interest_survey import PlantInterest

plant = PlantInterest.get_plants_interest


class WateringReminder:
    """
    docstring
    """

    _plant_water_amount = {
        "Kale": 1,
        "Cucumber": 0.5,
        "Basil": 0.75,
        "Tomato": 1,
    }  # measured in cups
    _plant_water_per_week = {
        "Kale": 2,
        "Cucumber": 3,
        "Basil": 4,
        "Tomato": 7,
    }  #
    _city = "Needham"
    _now = datetime.now()

    def __init__(self):
        """
        A dictionary connetcing name of the plant to the amount of watering per week
        """
        self.hum_const = 1
        self.precp_const = 0
        self.temp_const = 1
        self.weekdays_to_water = []
        self.water_frequency = 0
        self._now = datetime.now()
        plant_class = PlantInterest()
        self.plant = plant_class.get_plants_interest()
        self.preferred_watering_time = (
            plant_class.get_watering_time()
        )  # time at which user preferes to recive notifications
        self.kept_outside = plant_class.get_garden_location()
        self.days_to_water = self.time_to_water(
            self.plant, self.time_tracker_weekday()
        )

    def time_tracker_hour(self):
        """
        Docstring
        """
        hour = self._now.strftime("%H")
        return int(hour)

    def time_tracker_weekday(self):
        """
        Docstring
        """
        weekday = self._now.weekday()
        return weekday  # day of the week 0 being Monday and 6 being Sunday

    def amount_of_water(self, _city):
        """
        Determine the watering constants based on the weather conditions
        """
        temp = weather_data(_city)["temperature"]
        precp = weather_data(_city)["precipitation"]
        hum = weather_data(_city)["humidity"]
        if 60 < hum <= 100:
            self.hum_const = 0.75
        elif 40 < hum <= 60:
            self.hum_const = 1
        elif 20 < hum <= 40:
            self.hum_const = 1.25
        if precp >= 60:
            self.precp_const += 1
        if temp > 32:
            self.temp_const = 1.5
        elif 7 <= temp <= 32:
            self.temp_const = 1

    def calculating_watering(self, kept_outside, _plant_water_amount):
        """
        Calculate the amount of watring necessary based on the constants and
        amount defined in the dicitonary
        """
        if kept_outside is True:
            if self.precp_const == 1:
                return "Don't need to water"
        amount_of_water = _plant_water_amount * (
            (self.hum_const + self.temp_const) / 2
        )
        return amount_of_water

    def time_to_water(self, chosen_plant, weekday):
        """
        Calculate on which days to water
        """
        if self._plant_water_per_week[chosen_plant] == 1:
            self.weekdays_to_water.append(weekday)
        elif self._plant_water_per_week[chosen_plant] == 2:
            weekday_2 = weekday + 3
            if weekday_2 > 6:
                weekday_2 -= 6
            self.weekdays_to_water.append([weekday, weekday_2])
        elif self._plant_water_per_week[chosen_plant] == 3:
            weekday_2 = weekday + 2
            weekday_3 = weekday + 2
            if weekday_2 > 6:
                weekday_2 -= 6
            if weekday_3 > 6:
                weekday_3 -= 6
            self.weekdays_to_water.append([weekday, weekday_2, weekday_3])
        elif self._plant_water_per_week[chosen_plant] == 4:
            weekday_2 = weekday + 2
            weekday_3 = weekday + 2
            weekday_4 = weekday + 2
            if weekday_2 > 6:
                weekday_2 -= 6
            if weekday_3 > 6:
                weekday_3 -= 6
            if weekday_4 > 6:
                weekday_4 -= 6
            self.weekdays_to_water.append(
                [weekday, weekday_2, weekday_3, weekday_4]
            )
        elif self._plant_water_per_week[chosen_plant] == 5:
            weekday_2 = weekday + 2
            weekday_3 = weekday + 2
            weekday_4 = weekday + 2
            weekday_5 = weekday_4 + 1
            if weekday_2 > 6:
                weekday_2 -= 6
            if weekday_3 > 6:
                weekday_3 -= 6
            if weekday_4 > 6:
                weekday_4 -= 6
            if weekday_5 > 6:
                weekday_5 -= 6
            self.weekdays_to_water.append(
                [weekday, weekday_2, weekday_3, weekday_4, weekday_5]
            )
        elif self._plant_water_per_week[chosen_plant] == 6:
            weekday_2 = weekday + 2
            weekday_3 = weekday + 2
            weekday_4 = weekday + 2
            weekday_5 = weekday_4 + 1
            weekday_6 = weekday_3 + 1
            if weekday_2 > 6:
                weekday_2 -= 6
            if weekday_3 > 6:
                weekday_3 -= 6
            if weekday_4 > 6:
                weekday_4 -= 6
            if weekday_5 > 6:
                weekday_5 -= 6
            if weekday_6 > 6:
                weekday_6 -= 6
            self.weekdays_to_water.append(
                [weekday, weekday_2, weekday_3, weekday_4, weekday_5, weekday_6]
            )
        else:
            self.weekdays_to_water = [0, 1, 2, 3, 4, 5, 6]
        return self.weekdays_to_water

    def generate_message(self):
        """
        Docstring
        """
        if self.time_tracker_weekday() in self.days_to_water:
            if self.time_tracker_hour() == self.preferred_watering_time:
                self.amount_of_water(self._city)
                print(
                    f"it's time to water your {self.plant}. Please give your"
                    " plant"
                    f" {self.calculating_watering(self.kept_outside, self._plant_water_amount[self.plant])} cups"
                    " of water"
                )
