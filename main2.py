import http.client as http
http._MAXHEADERS = 1000
import os
from os.path import exists
import requests
import re
from geopy.geocoders import Nominatim
import subprocess, platform

if platform.system()=="Windows":
    subprocess.Popen("cls", shell=True).communicate() 
else: 
    print("\033c", end="")

def pingscrape(originserv):
    mystr = requests.get(url = 'https://wondernetwork.com/pings/' + originserv).text
    out = mystr.split("\n")
    #print("\n\nLatency In ms From New York\n")

    cityms = []

    with open('ping', 'w') as f:
                f.write("")

    for line in out:
        if 'href="/pings/New York/' in line:
            placere = re.search('k/(.*)"', line)
            place = placere.group(1)
            msre = re.search('>(.*)ms', line)
            ms = msre.group(1)
            ping = f"{place}:{ms}ms"

            cityms.append(ping)

    with open('ping', 'a') as f:
                for line in cityms:
                    f.write(line + "\n")


def cordscrape(originserv, target):
    import requests
    import re
    from geopy.geocoders import Nominatim

    mystr = requests.get(url = 'https://wondernetwork.com/pings/' + originserv).text
    out = mystr.split("\n")
    #print("\n\nLatency In ms From New York\n")
    citys = []
    cityms = []
    with open('citys', 'w') as f:
                f.write("")
    for line in out:
        print(line)
        if 'href="/pings/' + target + '/' in line:
            placere = re.search('k/(.*)"', line)
            place = placere.group(1)
            msre = re.search('>(.*)ms', line)
            ms = msre.group(1)
            ping = f"\n{place}: {ms}ms"
            citys.append(place)

    for line in citys:
        print(line)
    i = 0
    for item in citys:
        address=item
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(address)
        a = f"{item} : {location.latitude}, {location.longitude}"
        i = i + 1
        if start == 1:
            if platform.system()=="Windows":
                subprocess.Popen("cls", shell=True).communicate() 
            else: 
                print("\033c", end="")
            print("Hey there! thanks for using my program! Let the webscraper run fully, it usually lasts for 254 rows. Thankfully this is the only time you will have to do this, sorry my code is shit, i dont really want to refactor it. \n")
        print(str(i) + "      " + str(a + "\n"))
        if i == len(citys):
            print("All Done!")
        with open('citys', 'a') as f:
            f.write("\n" + a)


check = os.path.join(os.path.curdir, 'citys')
check2 = os.path.join(os.path.curdir, 'ping')
start = 0
origin = "New%20York"
origin2 = "New York"
if not exists(check) and exists(check2):
    start = 1
    pingscrape(origin)    
    cordscrape(origin, origin2)
else:
    start = 0
    x = input("run program/update your data (not needed) [1/2]:")
    if x == "1":
        ping = input("what is player ping: ")
        pingscrape(origin)
        import calculation
        import plotter
        calculation.main(ping)
        plotter.main('New York')
    if x == "2":
        pingscrape(origin)    
        cordscrape(origin, origin2)


 