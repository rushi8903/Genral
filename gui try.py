from cgitb import text
from tkinter.ttk import LabeledScale

import phonenumbers as pn
from phonenumbers import carrier, geocoder
from tkinter import OptionMenu, StringVar, Tk, Label, Button, Entry, mainloop, messagebox, END
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser
import os
window =Tk()
window.title("kuchh bhi")
window.geometry("450x450")
hii = Label(window, text="kya hai", font="Times", padx=70,pady= 10 ).pack()




window.mainloop()

# def sum(num):
#     if num==1 :
#         return 1
#     return sum(num-1)+num
    
# a = sum(100)
# print(a)



