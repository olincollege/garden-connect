from datetime import datetime


class Time:
    """
    Docstring
    """

    _now = datetime.now()


    def weekday_tracker(self, _now):
        """
        Docstring
        """
        weekday = (
            _now.weekday()
        )  # day of the week 0 being Monday and 6 being Sunday
        return weekday
