import datetime

class KitchenTimer:

    def __init__(self):
        self.reset()

    def addMinutes(self, minutes):
        if self.isRunning():
            return
        self._initialMinutes += minutes
        self._initialMinutes %= 100
        self._setTimer()

    def addSeconds(self, seconds):
        if self.isRunning():
            return
        self._initialSeconds += seconds
        self._initialSeconds %= 60
        self._setTimer()

    def _setTimer(self):
        self._totalInSeconds = self._initialMinutes * 60 + self._initialSeconds

    def reset(self):
        self._totalInSeconds = 0
        self._endTime = None
        self._initialMinutes = 0
        self._initialSeconds = 0
    
    def startOrStop(self):
        if self.isRunning():
            # stopping timer
            if self.shouldAlarm(): # timer expired
                self._setTimer()
            else: # still running, so suspending
                delta = self._endTime - datetime.datetime.now()
                self._totalInSeconds = delta.total_seconds()
            self._endTime = None
        else:
            # starting timer
            if self._totalInSeconds == 0:
                return # do nothing unless timer is set
            delta = datetime.timedelta(seconds=self._totalInSeconds)
            self._endTime = datetime.datetime.now() + delta
    
    def shouldAlarm(self):
        if self._endTime:
            return self._endTime < datetime.datetime.now()
        else:
            return False

    def isRunning(self):
        return self._endTime != None

    def getSeconds(self):
        self._update()
        return self._totalInSeconds

    def _update(self):
        if self.isRunning() and self._endTime and self._endTime > datetime.datetime.now():
            delta = self._endTime - datetime.datetime.now()
            self._totalInSeconds = delta.total_seconds()
