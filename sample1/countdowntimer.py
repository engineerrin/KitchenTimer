import time
import datetime

minutes = 2
seconds = 30
totalInSeconds = minutes * 60 + seconds

startTime = datetime.datetime.now()
endTime = startTime + datetime.timedelta(seconds=totalInSeconds)

print("Timer Started")
while endTime > datetime.datetime.now():
    now = datetime.datetime.now()
    remainingTotalSeconds = int((endTime - now).total_seconds())
    remainingMinutes = int(remainingTotalSeconds / 60)
    remainingSeconds = remainingTotalSeconds % 60
    timeToDisplay = f"{remainingMinutes:02d}:{remainingSeconds:02d}"
    print("\t" + timeToDisplay + "\r", end="")
    time.sleep(0.1)
print("\nIt's time!")
