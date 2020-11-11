#convert any number into hours and minutes
def to_hours_minutes(num):
    hours = num // 60
    minutes = num % 60
    hours_str = " hours"
    minutes_str = " minutes"

    if(hours == 1):
        hours_str = " hour"

    if(minutes == 1):
        minutes_str = " minute"

    return str(hours) + hours_str + ", " + str(minutes) + minutes_str
