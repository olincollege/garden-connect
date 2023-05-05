<<<<<<< HEAD
from plant_interest_survey import PlantInterest
=======
"""
Tests cases for plant interest survey
"""
from plant_interest_survey import PlantInterest # pylint: disable=E0401
from watering import WateringReminder
from time_storage import Time
import pytest
>>>>>>> 5142219da7458b77b3fd93c19bfc583647b05ce4

##### Test Cases ######


<<<<<<< HEAD
####### Test That Message is Being Generated Correctly ########
=======
interest = PlantInterest()
watering = WateringReminder()
time = Time()

### Tetst Cases ###

# Testing weather correct amount of water is being ouputted based on provided constants
time_to_water_cases = [
    # Plant that needs to be watered twise is watered twise
    # based on day that person registered for notifications
    (
        ["Kale", watering.time_to_water()], # pylint: disable=E1120
        [time.weekday_tracker(), (time.weekday_tracker() + 3)],
    ),
    # Plant that needs to be watered 3 times is getting watered
    # 3 times based on day that person registered for notifications
    (
        ["Cucumber", watering.time_to_water()], # pylint: disable=E1120
        [
            time.weekday_tracker(),
            (time.weekday_tracker() + 2),
            (time.weekday_tracker() + 4),
        ],
    ),
    #  Plant that needs to be watered 4 times is getting watered
    # 3 times based on day that person registered for notifications
    (
        ["Basil", watering.time_to_water()], # pylint: disable=E1120
        [
            time.weekday_tracker(),
            (time.weekday_tracker() + 2),
            (time.weekday_tracker() + 4),
            (time.weekday_tracker() + 6),
        ],
    ),
    #  Plant that needs to be watered 7 times is getting watered
    # 3 times based on day that person registered for notifications
    (
        ["Tomato", watering.time_to_water()], # pylint: disable=E1120
        [
            time.weekday_tracker(),
            (time.weekday_tracker() + 1),
            (time.weekday_tracker() + 2),
            (time.weekday_tracker() + 3),
            (time.weekday_tracker() + 4),
            (time.weekday_tracker() + 5),
            (time.weekday_tracker() + 6),
        ],
    ),
]

generate_message_cases = [
    ("Tomato", "It's time to check your Tomato"),
    ("Kale", "It's time to check your Kale"),
    ("Cucumber", "It's time to check your Cucumber"),
    ("Basil", "It's time to check your Basil"),
]

correct_weekday_message_cases = []

get_plant_cases = []

garden_location_cases = []

get_watering_time = []
>>>>>>> 5142219da7458b77b3fd93c19bfc583647b05ce4


def test_get_plant_ineterest(monkeypatch):
    """
    Test that correct plant is being saved

    Works by patching builtins.input
    """

    def mock_input_tomato(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "3"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_tomato)

    assert interest.get_plants_interest() == "Tomato"

    def mock_input_basil(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "4"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_basil)

    assert interest.get_plants_interest() == "Basil"

    def mock_input_cucumber(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "1"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_cucumber)

    assert interest.get_plants_interest() == "Cucumber"

    def mock_input_kale(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "2"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_kale)

    assert interest.get_plants_interest() == "Kale"

    #### Test time input ###


###########################################
###########################################
###########################################


def test_get_watering_time(monkeypatch):
    """
    Test that correct watering time is being stored

    Works by patching builtins.input
    """

    def mock_input_one_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "1"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_one_am)

    assert interest.get_watering_time() == 1

    def mock_input_two_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "2"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_two_am)

    assert interest.get_watering_time() == 2

    def mock_input_three_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "3"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_three_am)

    assert interest.get_watering_time() == 3

    def mock_input_four_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "4"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_four_am)

    assert interest.get_watering_time() == 4

    def mock_input_five_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "5"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_five_am)

    assert interest.get_watering_time() == 5

    def mock_input_six_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "6"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_six_am)

    assert interest.get_watering_time() == 6

    def mock_input_seven_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "7"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_seven_am)

    assert interest.get_watering_time() == 7

    def mock_input_eight_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "8"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_eight_am)

    assert interest.get_watering_time() == 8

    def mock_input_nine_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "9"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_nine_am)

    assert interest.get_watering_time() == 9

    def mock_input_ten_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "10"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_ten_am)

    assert interest.get_watering_time() == 10

    def mock_input_eleven_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "11"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_eleven_am)

    assert interest.get_watering_time() == 11

    def mock_input_twelve_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "12"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_twelve_pm)

    assert interest.get_watering_time() == 12

    def mock_input_one_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "13"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_one_pm)

    assert interest.get_watering_time() == 13

    def mock_input_two_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "14"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_two_pm)

    assert interest.get_watering_time() == 14

    def mock_input_three_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "15"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_three_pm)

    assert interest.get_watering_time() == 15

    def mock_input_four_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "16"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_four_pm)

    assert interest.get_watering_time() == 16

    def mock_input_five_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "17"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_five_pm)

    assert interest.get_watering_time() == 17

    def mock_input_six_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "18"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_six_pm)

    assert interest.get_watering_time() == 18

    def mock_input_seven_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "19"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_seven_pm)

    assert interest.get_watering_time() == 19

    def mock_input_eight_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "20"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_eight_pm)

    assert interest.get_watering_time() == 20

    def mock_input_nine_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "21"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_nine_pm)

    assert interest.get_watering_time() == 21

    def mock_input_ten_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "22"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_ten_pm)

    assert interest.get_watering_time() == 22

    def mock_input_eleven_pm(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "23"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_eleven_pm)

    assert interest.get_watering_time() == 23

    def mock_input_twelve_am(_):
        """
        Pretend to be a human behind a keyboard.

        args:
            _: A string representing the prompt positional argument given
                to input.
        """
        return "0"

    interest = PlantInterest()
    monkeypatch.setattr("builtins.input", mock_input_twelve_am)

    assert interest.get_watering_time() == 0
