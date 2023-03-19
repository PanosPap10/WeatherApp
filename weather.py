# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:01:16 2023

@author: papap
"""
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk, Image

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

# Load the image
image = Image.open("backG.jpg")
bg_image = ImageTk.PhotoImage(image)

# Create a label to hold the image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def getWeather():
    try:
        city = textField.get()
    
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f526e73b725ad90e50b0a4da73647f54"
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS", "LIKE", temp,"°"))
        
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry")


    
#search box
Search_image=PhotoImage(file="search_image_white.png")
myImage = Label(image=Search_image)
myImage.place(x=20,y=20)

#text field
textField = tk.Entry(root,justify="center", width=12, font=("poppins",25,"bold"), bg="white", border=0, fg="black")
textField.place(x=50, y=35)
textField.focus()

#search icon
Search_icon = PhotoImage(file="resized_search_icon.png")
myImage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="white", command=getWeather)
myImage_icon.place(x=320,y=35)

#logo
Logo_image = PhotoImage(file="resized_logo.png")
logo = Label(image=Logo_image)
logo.place(x=120,y=100)

#Bottom_box
Frame_image = PhotoImage(file="resized_box.png")
frame_myImage = Label(image=Frame_image)                       
frame_myImage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root, font=("arial",10,"bold"))
name.place(x=30,y=100)
clock = Label(root, font=("Helvetica",12))
clock.place(x=30,y=130)

#label
label1 = Label(root, text="WIND", font=("Helvetica",15,'bold'), fg="white", bg="#89CFF0")
label1.place(x=100,y=420)

label2 = Label(root, text="HUMIDITY", font=("Helvetica",15,'bold'), fg="white", bg="#89CFF0")
label2.place(x=250,y=420)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica",15,'bold'), fg="white", bg="#89CFF0")
label3.place(x=450,y=420)

label4 = Label(root, text="PRESSURE", font=("Helvetica",15,'bold'), fg="white", bg="#89CFF0")
label4.place(x=650,y=420)

t = Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

c = Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w = Label(text=". . .", font=("arial",20,"bold"),bg="#89CFF0")
w.place(x=100,y=450)

h = Label(text=". . .", font=("arial",20,"bold"),bg="#89CFF0")
h.place(x=270,y=450)

d = Label(text=". . .", font=("arial",20,"bold"),bg="#89CFF0")
d.place(x=430,y=450)

p = Label(text=". . .", font=("arial",20,"bold"),bg="#89CFF0")
p.place(x=670,y=450)

root.mainloop()












