import requests
import re
import sqlite3
from geopy.geocoders import Nominatim


geolocator = Nominatim()
conn = sqlite3.connect('wifi.db')
c = conn.cursor()


def create_db():
    c.execute('''CREATE TABLE wifi
             (address text, lat real, lng real)''')
    return("The table was created successfully.")


def get_db():
    for row in c.execute('SELECT * FROM wifi ORDER BY address'):
        print(row)


def get_wifi():
    """Extracts WiFi locations from a website and saves them into a database."""

    resp = requests.get("http://www.openwifispots.com/citylist_free_wifi_wireless_hotspot-Portland_OR.aspx")
    fulltext = resp.text
    middlecut = fulltext[fulltext.find("""<div id="location5952"""):fulltext.find("""Been here? <a href="javascript:addComment(265904)""")]
    multiple_commas = re.sub("<[^<]+?>", ",", middlecut)
    single_commas = re.sub(r"[,]+", ",", multiple_commas)[1:-1]
    result = single_commas.split(",Been here? ,Add a comment...,")

    for r in result:
        addresscut = r.split(",")
        for a in addresscut:
            if "..." in a:
                addresscut.remove(a)f
        address_total = addresscut[1] + ", " + addresscut[2] + "," + addresscut[3]

        try:
            location = geolocator.geocode(address_total, timeout=None)
            c.execute("INSERT INTO wifi VALUES (?, ?, ?)", (addresscut[0], location.latitude, location.longtitude)
            conn.commit()
            print("{} was saved into the database".format(addresscut[0]))
        except AttributeError:
            print("Couldn't convert this one: {}".format(address_total))
    conn.close()
    return("Finished manipulating data.")


def populate_db():
    """Populates the database from file, in case geopy throws timeout error."""

    f = open("wifi.txt", "r")
    for line in f:
        address = line.split("of America ")[0]
        lat = (line.split("of America ")[1]).split(" ")[0]
        lng = ((line.split("of America ")[1]).split(" ")[1]).split("\n")[0]
        c.execute("INSERT INTO wifi VALUES (?, ?, ?)", (address, lat, lng))
        conn.commit()
    conn.close()
    print("Data added successfully.")


print(create_db())
# print(get_wifi())
print(populate_db())
print(get_db())
