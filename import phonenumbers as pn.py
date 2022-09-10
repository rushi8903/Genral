import phonenumbers as pn
from phonenumbers import carrier, geocoder
from tkinter import OptionMenu, StringVar, Tk, Label, Button, Entry, messagebox, END
from opencage.geocoder import OpenCageGeocode
import folium
Key = "b699588bdfeb45709f08e341e3e55f4d"
geo = OpenCageGeocode(Key)
window = Tk()
window.title("Phone Number Tracker-Group 1")
window.geometry("450x450")
codes = ["+91", "+1", "+254", "+852", "+971", "+44", "+46", "+33"]
country_code = StringVar()
country_code.set(codes[0])

intro = Label(window, text="Choose a country code and enter a number.",
              padx=20, pady=5, font="Times").pack()
drop_down = OptionMenu(window, country_code, *codes).pack(pady=5)
my_entry = Entry(window, width=35, borderwidth=3, bg="black", fg="white", bd=5)
my_entry.pack()
run_prog = Button(window, text="Click me!", padx=10, pady=10, command=lambda: condition()).pack()

#input responses
def condition():
    response = my_entry.get()
    if response == "":
        messagebox.showerror("Error", "Please enter a number.")
    elif len(response) < 9 :
        messagebox.showerror("Error", "Enter a 10 digits number")
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
    show_provider = Label(window, text="Service provider: "+provider).pack()
    show_location = Label(window, text="Location: "+location +
                          " ("+str(coord[0]['components']['country_code'])+")").pack()
    show_lat = Label(window, text="Latitude: "+str(latitude)).pack()
    show_lng = Label(window, text="Longitude: "+str(longitude)).pack()
    show_timezone = Label(window, text="Timezone: " +
                          coord[0]['annotations']['timezone']['name']).pack()
    mymap = folium.Map(location=[latitude, longitude])
    folium.Marker([latitude, longitude], popup="Location").add_to(mymap)
    mymap.save("location.html")


window.mainloop()