import weather_module as wm
import tkinter as tk

def get_city():
    city = entry_1.get()
    data = wm.get_weather_info(city)

    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_5.delete(0, tk.END)

    entry_2.insert(0, f"{data[0]}°C")
    entry_3.insert(0,data[1])
    entry_4.insert(0,data[2])
    entry_5.insert(0,data[3])

#create a new window
window = tk.Tk()
window.configure(bg="white") # Sets background to light blue
window.title("DenSSS Weather API") 
window.geometry("720x600")

title = tk.Label(text="Weather System",
                 height = 2,
                 width = 35,
                 bg ="black",
                 fg = "green" 
)
title.config(font=("Arial", 32))
title.pack()
#*********************************************************************************

label_1 = tk.Label(text="Enter the name of the city:")
label_1.config(font=("Arial", 18))
label_1.pack()

entry_1 = tk.Entry(fg="black",
                    bg="lightblue",
                    width=36
)
entry_1.config(font=("tahoma",18,"bold"))
entry_1.pack()

button_1 = tk.Button(
    text="Find weather condition",
    width= 25,
    height=1,
    bg="gray",
    fg="white",
    command= get_city
)
button_1.config(font=("tahoma",14,"bold"))
button_1.pack()
#*********************************************************************************
label_2 = tk.Label(text="Temperature in °C:")
label_2.config(font=("Arial", 18))
label_2.pack()

entry_2= tk.Entry(fg="black",
                    bg="yellow",
                    width=32
)
entry_2.config(font=("tahoma",22,"bold"))
entry_2.pack()
#*********************************************************************************
label_3 = tk.Label(text="Description: ")
label_3.config(font=("Arial", 18))
label_3.pack()

entry_3 = tk.Entry(fg="black",
                    bg="yellow",
                    width=32
)
entry_3.config(font=("tahoma",22,"bold"))
entry_3.pack()
#*********************************************************************************
label_4 = tk.Label(text="Vision: ")
label_4.config(font=("Arial", 18))
label_4.pack()

entry_4 = tk.Entry(fg="black",
                    bg="yellow",
                    width=32
)
entry_4.config(font=("tahoma",22,"bold"))
entry_4.pack()
#*********************************************************************************
label_5 = tk.Label(text="Country Code: ")
label_5.config(font=("Arial", 18))
label_5.pack()

entry_5 = tk.Entry(fg="black",
                    bg="yellow",
                    width=32
)
entry_5.config(font=("tahoma",22,"bold"))
entry_5.pack()
#*********************************************************************************



window.mainloop()