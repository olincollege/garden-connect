from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
	NOTIFICATION_TYPES = ((1,'Like'),(2,'Comment'), (3,'Follow'))

	post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name="noti_post", blank=True, null=True)
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_from_user")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_to_user")
	notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
	text_preview = models.CharField(max_length=90, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)

class PlantInterest:
    """
    Docstring
    """

    def __init__(self):
        self.plants_interest = None
        self.garden_location = None
        self.watering_time = None

    def get_plants_interest(self):
        """
        Docstring
        """
        suggested_plants = ["Cucumber", "Kale", "Tomato", "Basil"]
        print("Which plant are you interested in?")
        for i, plant in enumerate(suggested_plants):
            print(f"{i+1}. {plant}")
        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit() and int(choice) in range(
            1, len(suggested_plants) + 1
        ):
            self.plants_interest = suggested_plants[int(choice) - 1]
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
        return suggested_plants[int(choice) - 1]

    def get_garden_location(self):
        """
        Docstring
        """
        location = input(
            "Do you plan to have a garden inside or outside? "
        ).strip()
        if location.lower() == "inside":
            self.garden_location = False
        elif location.lower() == "outside":
            self.garden_location = True
        else:
            print("Invalid input. Please enter 'inside' or 'outside'.")
        return self.garden_location

    def get_watering_time(self):
        """
        Docstring
        """
        time = input(
            "What time of day (0-23) is best for watering your plants? "
        ).strip()
        while not time.isdigit() or int(time) not in range(0, 24):
            print("Invalid input. Please enter a number between 0 and 23.")
            time = input(
                "What time of day (0-23) is best for watering your plants? "
            )
        return int(time)

    def get_user_input(self):
        """
        Docstring
        """
        self.get_plants_interest()
        self.get_garden_location()
        self.get_watering_time()
