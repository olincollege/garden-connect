from datetime import datetime


class Time: # pylint: disable=R0903
    """
    Storage of time for plant reminders
    """

    def weekday_tracker(self):
        """
        Evaluates the current time to determine what day of the week it is

        Returns:
            The current weekday according to the user's time standard
        """
        _now = datetime.now()
        weekday = _now.weekday()  # day of the week 0 being Monday and 6 being Sunday
        return weekday
