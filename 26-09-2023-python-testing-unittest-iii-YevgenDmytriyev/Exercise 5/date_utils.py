# date_utils.py

from datetime import datetime, timedelta

def get_future_date(current_date, days):
    """
    Calculate the date that is 'days' days in the future from the 'current_date'.

    Args:
        current_date (datetime): The current date.
        days (int): The number of days to add to the current date.

    Returns:
        datetime: The future date.
    """
    future_date = current_date + timedelta(days=days)
    return future_date

def is_weekend(date):
    """
    Check if a given date falls on a weekend (Saturday or Sunday).

    Args:
        date (datetime): The date to check.

    Returns:
        bool: True if the date is a weekend, False otherwise.
    """
    return date.weekday() in [5, 6]  # 5 represents Saturday, and 6 represents Sunday
