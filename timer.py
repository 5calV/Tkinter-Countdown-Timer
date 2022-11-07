
#--------------------------------------------------------------------------------------------------------------------------------------------

#   ╭∩╮     ╭∩╮
#    \(͡⚈ᴗ͡⚈)/

#--------------------------------------------------------------------------------------------------------------------------------------------

# Modules

from tkinter import*
from tkinter import messagebox
import time

#---------------------------------------------------------------------------------------------------------------------------------------

# Tkinter Main Window.

window = Tk()
  
window.geometry("300x250")
window.title("calV s Countdown App")

#---------------------------------------------------------------------------------------------------------------------------------------

# Variables

hour=StringVar()
minute=StringVar()
second=StringVar()



# Default Values.
hour.set("00")
minute.set("01")
second.set("00")



# User Input.
hourEntry= Entry(window, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=80,y=20)
  
minuteEntry= Entry(window, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=20)
  
secondEntry= Entry(window, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=20)
  


def submit():
    try:

# the user input is stored in "temp".
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         

        mins,secs = divmod(temp,60)



# Converting the Input.
        hours=0
        if mins >60:
             
            hours, mins = divmod(mins, 60)
        

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))



# Updating the GUI every time after the temp value has been decreased.
        window.update()
        time.sleep(1)



# A window with a message pops up when the temp value equals zero.
        if (temp == 0):
            messagebox.showinfo("calV s Countdown App", "Your time is over! ")
         

        
# After every second the temp value is decreased by one.
        temp -= 1



# Button
btn = Button(window, text='Start the Countdown', bd='5',
             command= submit)
btn.place(x = 70,y = 120)
  
window.mainloop()
