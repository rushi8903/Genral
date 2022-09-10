from cgitb import text
import phonenumbers as pn
from phonenumbers import carrier, geocoder
from tkinter import OptionMenu, StringVar, Tk, Label, Button, Entry, messagebox, END
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser
import os

Key = "2c8bdf19b1944a18a24e2a81fe2b0a9d"
geo = OpenCageGeocode(Key)
window = Tk()
window.title("Tracker by Group-4")
window.geometry("450x450")
codes = ["+91", "+1", "+254", "+852", "+971", "+44", "+46", "+33"]
country_code = StringVar()
country_code.set(codes[0])

intro = Label(window, text="Choose a country code and enter a number.",
              padx=40, pady=10, font="Times").pack()
drop_down = OptionMenu(window, country_code, *codes).pack(pady=20)
my_entry = Entry(window, width=35, borderwidth=3,
                 bg="Light blue", fg="black", bd=5)
my_entry.pack()
run_prog = Button(window, text="Find", padx=10, pady=10,
                  bg="Light yellow", command=lambda: condition()).pack()


def condition():
    response = my_entry.get()
    if response == "":
        messagebox.showerror("Error", "Please enter a number.")
    elif len(response) > 10:
        messagebox.showerror("Error", "Enter 10 digits")
    elif len(response) < 10:
        messagebox.showerror("Error", "Enter 10 digits")
    else:
        info()


def info():      
        response = my_entry.get()
        code = country_code.get()
        parsed = pn.parse(code+response)
        provider = carrier.name_for_number(parsed, 'en')
        location = geocoder.description_for_number(parsed, "en")
        coord = geo.geocode(str(location))
        latitude = coord[0]['geometry']['lat']
        longitude = coord[0]['geometry']['lng']
        sp = Label(window, text="Service provider: "+provider)
        sp.pack()
        l = Label(window, text="Location: "+location +
            " ("+str(coord[0]['components']['country_code'])+")")
        l.pack()
        la = Label(window, text="Latitude: "+str(latitude))
        la.pack()
        lo = Label(window, text="Longitude: "+str(longitude))
        lo.pack()
        t = Label(window, text="Timezone: " +
            coord[0]['annotations']['timezone']['name'])
        t.pack()
        mymap = folium.Map(location=[latitude, longitude])
        folium.Marker([latitude, longitude], popup="Location").add_to(mymap)
        mymap.save("location.html")
        filename = 'file:///'+os.getcwd()+'/' + 'location.html'
        webbrowser.open_new_tab(filename)
        def remove():
            sp.destroy()
            l.destroy()
            la.destroy()
            lo.destroy()
            t.destroy()
            b.destroy()
        b = Button(window, text="Clear", command=remove)
        b.pack()
        


window.mainloop()