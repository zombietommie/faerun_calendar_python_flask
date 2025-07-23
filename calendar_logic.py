# A dictionary to hold the special holidays that fall between months.
# The key is the month number *before* the holiday.
# For example Midwinter is between month 12 and 1.

HOLIDAYS = {
        0: "Midwinder",
        3: "Greengrass",
        6: "Midsummer",
        9: "Highharvestide",
        12: "The Feast of the Moon",
}

# A list of the 12 months, in order.
MONTHS = [
        "Hammer",
        "Alturiak",
        "Ches",
        "Tarsakh",
        "Mirtul",
        "Kythorn",
        "Flamerule",
        "Eleasis",
        "Eleint",
        "Marpenoth",
        "Uktar",
        "Nightal",
]

def get_month_name(month_number):
    """Returns the name of a month from its number (1-12)."""
    if 1 <= month_number <= 12:
        return MONTHS[month_number -1]
    return None

def get_holiday_after_month(month_number):
    """Returns the name of a holiday following a given month number."""
    return HOLIDAYS.get(month_number)

def is_leap_year(year):
    """Shieldmeet occurs in years divisible by 4."""
    return year % 4 == 0
