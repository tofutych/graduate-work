import datetime


def year_choices():
    return [(year, year) for year in range(2015, datetime.date.today().year + 1)]
