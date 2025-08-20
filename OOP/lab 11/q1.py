class Time:
    def __init__(self):

        self.__hour = 0
        self.__min  = 0

    def __init__(self, hour, min):

        self.__hour = hour
        self.__min  = min

    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min):
        self.__min = min


    def printTime(self):
        print(f"The time is {self.__hour} : {self.__min}")



class Date:
    def __init__(self):
        self.__month = 0
        self.__day   = 0
        self.__year  = 0

    def __init__(self, month, day, year):
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
        print(f"The date is ${self.__month} {self.__day} {self.__year}")

    
class Event:

    def __init__(self, hours = 0, min = 0, month = 1, day = 1, year=2000, eventName = "Eid"):
        self.__eventName = eventName
        self.eventTime = Time(hours, min)
        self.eventDate  = Date(month, day, year)


    def setEventData(self, hours, min, month, day, year, eventName):
        self.__eventName = eventName
        
        self.eventTime.hour = hours
        self.eventTime.min  = min

        self.eventDate.month = month
        self.eventDate.day   = day
        self.eventDate.year  = year

    def printEventData(self):

        print(f"The name of the event is {self.__eventName}")
        print(f"The date is {self.eventDate.month}{self.eventDate.day}{self.eventDate.year}")
        print(f"The Time is {self.eventTime.hour}:{self.eventTime.min}")



        
    
event = Event(10, 30, 12, 25, 2025, "Christmas")
event.printEventData()
event.setEventData(8, 0, 5, 1, 2026, "Eid")
event.printEventData()
    


    

    

    

    

