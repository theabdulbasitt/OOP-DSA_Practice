class Time:
    def __init__(self, hour=0, minute=0):
        self.__hour = hour
        self.__minute = minute

    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        self.__minute = minute

    def printTime(self):
        print(f"The time is {self.__hour}:{self.__minute}")


class Date:
    def __init__(self, month=1, day=1, year=2000):
        self.__month = month
        self.__day   = day
        self.__year  = year

    @property
    def month(self):
        return self.__month
    
    @month.setter
    def month(self, month):
        self.__month = month

    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day):
        self.__day = day

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year

    def printDate(self):
        print(f"The date is {self.__month}/{self.__day}/{self.__year}")


class Event:
    # Aggregation: Event takes Date and Time objects instead of creating them
    def __init__(self, eventName, timeObj, dateObj):
        self.__eventName = eventName
        self.eventTime = timeObj   # Aggregation: not owned, just referenced
        self.eventDate = dateObj   # Aggregation: can be shared

    def setEventData(self, eventName, timeObj, dateObj):
        self.__eventName = eventName
        self.eventTime = timeObj
        self.eventDate = dateObj

    def printEventData(self):
        print(f"The name of the event is {self.__eventName}")
        print(f"The date is {self.eventDate.month}/{self.eventDate.day}/{self.eventDate.year}")
        print(f"The time is {self.eventTime.hour}:{self.eventTime.minute}")


# ----------------- Testing Aggregation -----------------

# Create a single Date and Time
christmas_date = Date(12, 25, 2025)
morning_time = Time(10, 30)

# Share them across two events
event1 = Event("Christmas Party", morning_time, christmas_date)
event2 = Event("Christmas Dinner", morning_time, christmas_date)

# Print both
event1.printEventData()
event2.printEventData()

# Update shared objects
christmas_date.year = 2030
morning_time.hour = 11

print("\nAfter updating shared Date and Time:")
event1.printEventData()
event2.printEventData()
