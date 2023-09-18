secondsInDay = 60 * 60 * 24
secondsInHour = 60 * 60
secondsInMinute = 60


defsecondsToDays(seconds):
    return seconds // secondsInDay


def secondsToHours(seconds):
    return seconds // secondsInHour


def secondsToMinutes(seconds):
    return seconds // secondsInMinute


def secondsToSeconds(seconds):
    return seconds % secondsInMinute


formatters = (
    (secondsToDays, secondsInDay),
    (secondsToHours, secondsInHour),
    (secondsToMinutes, secondsInMinute),
    (secondsToSeconds, 1)
)


def formatSecondsDuration(durationInSeconds):
    seconds = durationInSeconds
    units = []

    for formatter, multiplier in formatters:
        unit = formatter(seconds)
        seconds -= unit * multiplier
        units.append(str(unit).zfill(2))

    return ':'.join(units)


print(formatSecondsDuration(3600))