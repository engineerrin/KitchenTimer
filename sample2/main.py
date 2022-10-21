import tkinter
import kitchentimerui

root = tkinter.Tk()
root.title("Multiple Kitchen Timer")

timer1 = kitchentimerui.KitchenTimerUI(root, 'cyan')
timer1.frame.pack()
timer2 = kitchentimerui.KitchenTimerUI(root, 'pink')
timer2.frame.pack()

def update():
    timer1.update()
    timer2.update()
    root.after(100, update)

update()
root.mainloop()
