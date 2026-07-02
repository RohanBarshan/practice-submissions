class MyCalendar:
    
    def __init__(self):
        self.event = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.event:
            if startTime < end and start < endTime:
                return False
        self.event.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)