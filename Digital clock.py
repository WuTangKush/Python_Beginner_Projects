import tkinter as tk
import time

class clock:
    def __init__(self):
        self.master = tk.Tk()

    def settings(self):
        self.master.title("My Clock")

    def widgets(self):
        def counttime(time1 = ''):
            time2 = time.strftime("%H:%M:%S")
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
                clock.after(200, counttime)

        #create clock text
        clock =tk.Label(self.master, font = ("Poppins", 50, "bold"),
          background ="black", 
          foreground="white")
        clock.pack(anchor="center")
        #clock loop
        counttime()
        tk.mainloop()
if __name__ =="__main__":
    my_clock = clock()
    my_clock.settings()
    my_clock.widgets()
      

