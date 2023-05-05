"""
Implementation of the watering schedule to follow for a plant
"""
from datetime import datetime
from plant_interest_survey import PlantInterest # pylint: disable=E0401

plant = PlantInterest.get_plants_interest


class WateringReminder:
    """
    Attributes:
        weekdays_to_water: list
            A list of weekdays on which the plant needs to be watered.
        water_frequency: int
            The number of times the plant needs to be watered in a week.
        plant: str
            The name of the plant whose watering needs to be reminded.
        preferred_watering_time: int
            The time at which the user prefers to receive notifications.
        days_to_water: list
            A list of weekdays on which the plant needs to be watered based on its watering frequency.

    Methods:
        time_tracker_hour()
            Returns the current hour of the day.
        time_tracker_weekday()
            Returns the current day of the week.
        time_to_water(chosen_plant, weekday)
            Calculates on which days the chosen plant needs to be watered based on its watering frequency.
        generate_message()
            Generates a message to remind the user to water their plant at the preferred watering time.
    """

    # Dictionary of plants linked to the number of times they need to be checked per week
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
        Initializes the WateringReminder class instance by setting the
        plant name, the preferred watering time, and
        the days on which the plant needs to be watered based on its watering frequency.
        """
        self.weekdays_to_water = []
        self.water_frequency = 0
        self._now = datetime.now()
        plant_class = PlantInterest()
        self.plant = plant_class.get_plants_interest()
        self.preferred_watering_time = (
            plant_class.get_watering_time()
        )  # time at which user preferes to recive notifications
        self.days_to_water = self.time_to_water(self.plant, self.time_tracker_weekday())

    def time_tracker_hour(self):
        """
        Returns the current hour of the day as an integer.
        """
        hour = self._now.strftime("%H")
        return int(hour)

    def time_tracker_minute(self):
        """
        Returns the current minute of the day as an integer.
        """
        minute = self._now.strftime("%M")
        return int(minute)

    def time_tracker_weekday(self):
        """
        Returns the current day of the week as an integer (Monday = 0, Sunday = 6).
        """
        weekday = self._now.weekday()
        return weekday  # day of the week 0 being Monday and 6 being Sunday

    def time_to_water(self, chosen_plant, weekday):
        """
        Calculates on which days the chosen plant needs to be watered based on its watering frequency.

        Parameters:
            chosen_plant (str):
                The name of the plant whose watering frequency is to be checked.
            weekday (int):
                The current day of the week (Monday = 0, Sunday = 6).

        Returns:
            list: A list of weekdays on which the plant needs to be watered based on its watering frequency.
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
            weekday_3 = weekday_2 + 2
            if weekday_2 > 6:
                weekday_2 -= 6
            if weekday_3 > 6:
                weekday_3 -= 6
            self.weekdays_to_water.append([weekday, weekday_2, weekday_3])
        elif self._plant_water_per_week[chosen_plant] == 4:
            weekday_2 = weekday + 2
            weekday_3 = weekday_2 + 2
            weekday_4 = weekday_3 + 2
            if weekday_2 > 6:
                weekday_2 -= 6
            if weekday_3 > 6:
                weekday_3 -= 6
            if weekday_4 > 6:
                weekday_4 -= 6
            self.weekdays_to_water.append([weekday, weekday_2, weekday_3, weekday_4])
        elif self._plant_water_per_week[chosen_plant] == 5:
            weekday_2 = weekday + 2
            weekday_3 = weekday_2 + 2
            weekday_4 = weekday_3 + 2
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
            weekday_3 = weekday_2 + 2
            weekday_4 = weekday_3 + 2
            weekday_5 = weekday_2 + 1
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
<<<<<<< HEAD
        Generates a message to be prited to remimd user to water their plant
=======
        Outputs a formatted message for appropriate conditioning
        of a plant
>>>>>>> 5142219da7458b77b3fd93c19bfc583647b05ce4
        """
        if self.time_tracker_weekday() in self.days_to_water:
            if self.time_tracker_hour() == self.preferred_watering_time:
                if self.time_tracker_minute() == 0:
                    print(f"It's time to check your {self.plant}.")
