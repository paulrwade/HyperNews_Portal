from datetime import datetime


def get_week_number(datetime_obj):
    return "Week number: " + datetime_obj.strftime("%U") + "."
