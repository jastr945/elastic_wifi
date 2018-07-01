import requests
import re
from geopy.geocoders import Nominatim


geolocator = Nominatim()

def get_wifi():
    """Extracts WiFi locations from a website and saves them into a text file."""

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
                addresscut.remove(a)
        address_total = addresscut[1] + ", " + addresscut[2] + "," + addresscut[3]
        try:
            location = geolocator.geocode(address_total, timeout=None)
            print(location.address, location.latitude, location.longitude, "\n")
        except AttributeError:
            print("Couldn't convert this one: {}".format(address_total))


print(get_wifi())
