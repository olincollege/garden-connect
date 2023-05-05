"""
Tests cases for plant interest survey
"""
from plant_interest_survey import PlantInterest # pylint: disable=E0401
from watering import WateringReminder
from time_storage import Time
import pytest

####### Creating class instances######


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


##### Test Functions ######


@pytest.mark.parametrize(
    "[plant, current_weekday], watering_weekdays",
    time_to_water_cases,
)
def test_calculating_watering(plant, current_wekday, watering_weekdays):
    """
    Check that correct days are being appended based on the day
    that person registerd for the notifications and number of days per
    week that plant needs to be checked
    """
    assert watering.time_to_water(plant, current_wekday) == watering_weekdays


@pytest.mark.parametrize(
    "plant, watering_message",
    generate_message_cases,
)
def test_generate_message(plant, watering_message):
    """
    Check that geneated messages are gene
    """
    assert helper_generate_message(plant) == watering_message


def helper_generate_message(plant_name):
    """
    Docstring
    """
    watering.plant = plant_name
    return watering.generate_message()


# @pytest.mark.parametrize(
#     "[is_outside, input_watering_amount], necessary_watering_amount",
#     calculating_watering_cases,
# )
# def test_calculating_watering(is_outside, watering_amount, necessary_watering_amount):
#     """
#     Docstring Here
#     """
#     assert (
#         watering.calculating_watering(watering, is_outside, watering_amount)
#         == necessary_watering_amount
#     )
