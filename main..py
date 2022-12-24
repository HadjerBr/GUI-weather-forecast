from tkinter import *
import weather



city = ""
city_name = ""
temperature = ""
date_and_time= ""
sky = ""
precipitation = ""
humidity = ""
wind = ""



root = Tk()
root.title("weather forecast")
root.iconbitmap("icons/sunny.ico")
root.resizable(0, 0)
root.configure(bg="sky blue")
frame = Frame(root)
frame.pack()
label = Label(frame, text="Enter a city name:")
label.grid(row=1, column=0, padx=20, pady=5 )
entry = Entry(frame)
entry.grid(row=1, column=1)
button = Button(frame, text="today's weather?", highlightthickness=0, command= lambda: print_weather())
button.grid(row=1, column=2, padx=20, pady=5 )
label2 = Label(frame, text = "")
label2.grid(row=2, column=0, columnspan=3, padx=20, pady=10)
label2.configure(text="Weather will appear here")
def print_weather():
    global city
    global city_name, temperature, date_and_time, sky, precipitation, humidity, wind
    city = entry.get()
    weather.get_weather(city)
    wind = weather.wind
    city_name = weather.city_name
    temperature = weather.temperature
    date_and_time = weather.date_and_time
    sky = weather.sky
    precipitation = weather.precipitation
    humidity = weather.humidity
    result = f"{city}\n{date_and_time}\nSky: {sky}\t\t\t\tTemperature:{temperature} c°\n\t\t\t\t\tHumidity:{humidity}\n\t\t\t\t\tWind: {wind}"
    label2.configure(text=result)




root.mainloop()