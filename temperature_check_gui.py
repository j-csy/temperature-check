import tkinter as tk
import string
import requests

from tkinter import messagebox
from tkinter import *


def get_weather():
    API_key = "12549cfffc93587bf8216ce33e6739c5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Sydney" 
    Final_url = base_url + "appid=" + API_key + "&q=" + city_name

    weather_data = requests.get(Final_url).json()

    #convert Kelvin to Celsius and round 2 decimals
    curTempC = round(weather_data['main']['temp'] - 273.15)

    return (curTempC)



def close_window():
    if (messagebox.askquestion("Confirm","Are you sure?")) == 'yes':
        window.destroy()

        

def Threshold_check(temp, tempno):
    #Threshold
    minTemp = 30
    maxTemp = 90


    if int(temp) < minTemp:
        

        reset = "".join( ""  for x in range(50))
        msgLabel['text'] = reset
        if tempno == 1:
            messagebox.showwarning("WARNING",str(tempno) + "st Temperature below threshold (30C) !!!")
        elif tempno == 2:
            messagebox.showwarning("WARNING",str(tempno) + "nd Temperature below threshold (30C) !!!")
            
        
    elif int(temp) > maxTemp:

        if tempno == 1:
            messagebox.showwarning("WARNING",str(tempno) + "st Temperature above threshold (90C) !!!")
        elif tempno == 2:
            messagebox.showwarning("WARNING",str(tempno) + "nd Temperature above threshold (90C) !!!")
     
def DecInc_check(temp1, temp2):
    if temp1 > (temp2 + 20) :
        messagebox.showwarning("ALARM","DECREASE more than 20C !!!. \n Try again. ")
    elif temp1 < (temp2 - 20) :
        messagebox.showwarning("ALARM","INCREASE more than 20C !!!. \n Try again. ")
    else:
        messagebox.showinfo("Info","Temperature within range. Try again. ")


def processTemp():
    reset = "".join( ""  for x in range(50))
    msgLabel['text'] = reset
 
    try:
        Temp1= int(entTemp1.get())
        Temp2= int(entTemp2.get())

        
        # Verify threshold    
        Threshold_check(entTemp1.get(), 1)
        Threshold_check(entTemp2.get(), 2)
        
        # Verify increase/decreas from previous temperature
        DecInc_check(Temp1, Temp2)
        
    except ValueError:
        messagebox.showerror("Error!","Please enter the value in integer")

window = tk.Tk()
window.geometry('500x250')
window.title("Temperature Verification")
inputTemp1 = tk.IntVar()
inputTemp2 = tk.IntVar()

topFrame = Frame(window)
msgLabel = Label(topFrame)
msgLabel.grid(row=2,column=5)



lblInitial = Label(window, text="Please enter Temperature :",)
lblInitial.grid(row=1,column=0)

#labels
lblTemp1 = Label(window, text="1st Temperature : ",).grid(row=2,column=0,)
lblTemp2 = Label(window, text="2nd Temperature: ",).grid(row=3,column=0,)
# An empty Label to force row to be displayed
#tk.Label(window).grid(row=4, column=0, columnspan=5)

lblTempOri = Label(window, text="Current temperature(C) : ",).grid(row=5,column=0)
 
#entries
entTemp1 = tk.Entry(window, textvariable=inputTemp1, width=5)  
entTemp1.grid(row=2,column=1)

entTemp2 = tk.Entry(window, textvariable=inputTemp2, width=5) 
entTemp2.grid(row=3,column=1)

# An empty Label to force row to be displayed
#tk.Label(window).grid(row=4, column=0, columnspan=5)

#display current temperature
gw = get_weather()
entTempOri = Label(window, text=gw, width=5)
#E2 = Entry(window, bd =5)
entTempOri.grid(row=5,column=1)

 # An empty Label to force row to be displayed
tk.Label(window).grid(row=6, column=0, columnspan=5)

#submit button
btnSubmit = Button(window, text ="Verify", command = processTemp)
btnSubmit.grid(row=4, column=1, padx=5, pady=5)



#exit button
Button(window, text ="Exit",width=10, command=close_window).grid(row=8,column=0)
 
window.mainloop()
