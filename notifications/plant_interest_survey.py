class PlantInterest:
    """
    Docstring
    """

    def __init__(self):
        self.plants_interest = None
        self.watering_time = None

    def get_plants_interest(self):
        """
        Asks the user which plant they are interested in and sets the `plants_interest` attribute to the selected plant.

        This method displays a list of suggested plants and prompts the user to select one. The user's choice is validated
        to ensure it is a number between 1 and the number of suggested plants. If the input is valid, the `plants_interest`
        attribute is set to the selected plant and the method

        Returns :
            A string of the selected plant. If the input is invalid, an error
            message is displayed and the method returns `None`.
        """
        suggested_plants = ["Cucumber", "Kale", "Tomato", "Basil"]
        print("Which plant are you interested in?")
        for i, plant in enumerate(suggested_plants):
            print(f"{i+1}. {plant}")
        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit() and int(choice) in range(1, len(suggested_plants) + 1):
            self.plants_interest = suggested_plants[int(choice) - 1]
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
        return suggested_plants[int(choice) - 1]

    def get_watering_time(self):
        """
        Prompts the user to enter the time of day when it is best to water their plants.

        This method asks the user to enter a number between 0 and 23 to represent the time of day when it is best to water
        their plants. The input is validated to ensure it is a valid integer within the range. If the input is invalid,
        an error message is displayed and the user is prompted again. Once a valid input is provided, the method returns the
        integer value.

        Return:
            An integer value representing the time of day when it is best to water the plants.
        """
        time = input(
            "What time of day (0-23) is best for watering your plants? "
        ).strip()
        while not time.isdigit() or int(time) not in range(0, 24):
            print("Invalid input. Please enter a number between 0 and 23.")
            time = input("What time of day (0-23) is best for watering your plants? ")
        return int(time)

    def get_user_input(self):
        """
        Asks the user for input on the plants they are interested in and the best time to water them.

        This method calls the `get_plants_interest` and `get_watering_time` methods to prompt the user for input on the plants
        they are interested in and the best time of day to water them. The `plants_interest` and `watering_time` attributes
        of the instance are set to the values returned by the respective methods.

        Return:
            None
        """
        self.get_plants_interest()
        self.get_watering_time()
