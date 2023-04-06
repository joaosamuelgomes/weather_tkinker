import tkinter as tk
from tkinter import *
from geopy.geocoders import Nominatim
from api_key import API_KEY
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Previsão do tempo")
root.state("zoomed")
root.resizable(False, False)

def getWeather():
    try:
        city=campotexto.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home=pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        relogio.config(text=current_time)
        nome.config(text="TEMPERATURA ATUAL")

        #clima
        api="https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid="+API_KEY

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"]-273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|","Sensação","Térmica",temp, "°C"))

        v.config(text=(wind, "m/s"))
        u.config(text=(humidity, "%"))
        p.config(text=(pressure, "hPa"))
    except Exception as e:
        messagebox.showerror("Previsão do tempo", "Não foi possível encontrar dados!")

#logo
logo_image = PhotoImage(file="assets\Logo.png")
logotipo = Label(image=logo_image)
logotipo.place(relx=0.5, rely=0.2, anchor="center")

#barra de pesquisa
barra_image = PhotoImage(file="assets\Bar.png")
barrapesquisa = Label(image=barra_image)
barrapesquisa.place(relx=0.5, rely=0.45, anchor="center")

campotexto = tk.Entry(root, justify="left", width=40, font=("Mate SC", 24, "bold"), bg="#F8F8F8", border=0, fg="black")
campotexto.place(relx=0.46, rely=0.45, anchor="center")
campotexto.focus()

pesquisa_image = PhotoImage(file="assets\Lupa.png")
lupa_icon = Button(image=pesquisa_image, borderwidth=0, cursor="hand2", bg="#f8f8f8", fg="black", command=getWeather)
lupa_icon.place(x=1030, y=320)

#rodape
rodape_image = PhotoImage(file="assets\Container.png")
rodape = Label(image=rodape_image)
rodape.pack(padx=5, pady=5, side=BOTTOM)

#horario
nome = Label(root, font=("arial", 15, "bold"))
nome.place(x=30, y=30)
relogio = Label(root, font=("Mate SC",20))
relogio.place(x=30, y=60)

#campos
campo1 = Label(root, text="VENTO", font=("Mate SC",15,"bold"), bg="#24CAFF", fg="white", justify="center")
campo1.place(x=360, y=640)

campo2 = Label(root, text="UMIDADE", font=("Mate SC",15,"bold"), bg="#24CAFF", fg="white", justify="center")
campo2.place(x=630, y=640)

campo4 = Label(root, text="PRESSÃO", font=("Mate SC",15,"bold"), bg="#24CAFF", fg="white", justify="center")
campo4.place(x=900, y=640)

t=Label(font=("arial",35,"bold"), fg="#ee666d")
t.place(relx=0.5, rely=0.58, anchor="center")
c=Label(font=("arial",35,"bold"))
c.place(relx=0.5, rely=0.65, anchor="center")

v=Label(text="...", font=("arial",20,"bold"), bg="#24caff")
v.place(x=360, y=670)
u=Label(text="...", font=("arial",20,"bold"), bg="#24caff")
u.place(x=630, y=670)
p=Label(text="...", font=("arial",20,"bold"), bg="#24caff")
p.place(x=900, y=670)






root.mainloop()