from datetime import datetime


class Time:
    """
    Docstring
    """

    def weekday_tracker(self):
        """
        Docstring
        """
        _now = datetime.now()
        weekday = _now.weekday()  # day of the week 0 being Monday and 6 being Sunday
        return weekday
