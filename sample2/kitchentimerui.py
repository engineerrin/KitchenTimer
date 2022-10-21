import tkinter
import math
import kitchentimer

class KitchenTimerUI:

    def __init__(self, parent, color):
        self.timer = kitchentimer.KitchenTimer()
        self.frame = tkinter.Frame(parent, bg=color)
        self.timeText = tkinter.StringVar()
        self.timeText.set('00:00')
        self.timeLabel = tkinter.Label(self.frame, textvariable=self.timeText, bg='gray', font=('Helvetica', 30))
        self.timeLabel.pack()
        row1 = tkinter.Frame(self.frame)
        row1.pack()
        tkinter.Button(row1, text='分', highlightbackground=color, command=lambda: self.timer.addMinutes(1)).pack(side = tkinter.LEFT)
        tkinter.Button(row1, text='秒', highlightbackground=color, command=lambda: self.timer.addSeconds(1)).pack(side = tkinter.LEFT)
        tkinter.Button(row1, text='リセット', highlightbackground=color, command=lambda: self.timer.reset()).pack(side = tkinter.LEFT)
        tkinter.Button(self.frame, text='スタート・ストップ', highlightbackground=color, command=lambda: self.timer.startOrStop()).pack()

    def update(self):
        time = math.ceil(self.timer.getSeconds())
        minutes = int(time / 60)
        seconds = int(time % 60)
        self.timeText.set(f'{minutes:02d}:{seconds:02d}')

        if self.timer.isRunning():
            self.timeLabel.config(bg='blue')
        else:
            self.timeLabel.config(bg='gray')

        if self.timer.shouldAlarm():
            self.timeLabel.config(bg='red')
            self.timeText.set("It's time")

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Kitchen Timer UI test")
    timerUI = KitchenTimerUI(root, 'cyan')
    timerUI.frame.pack()

    def update():
        timerUI.update()
        root.after(100, update)

    update()
    root.mainloop()
