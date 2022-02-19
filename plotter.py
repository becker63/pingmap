import folium
from geopy.geocoders import Nominatim

def main(origin5):

        testmap = folium.Map(location=[0, 0])

        geolocator = Nominatim(user_agent='myapplication')
        location1 = geolocator.geocode(origin5)
        location1.latitude

        folium.Circle(location=[location1.latitude, location1.longitude], popup='Origin Server', fill_color='#8332a8', radius=200000, weight=2, color="#8332a8").add_to(testmap)

        import numpy as np
        import re
        from termcolor import colored
        cords = []


        f = open('citys', 'r')
        citys = (f.read()).split("\n")
        

        f = open('output', 'r')
        checked = tuple((f.read()).split("\n"))
        lot = []

        for item2 in citys:
                split1 = item2.split(":")
                #print(split1)
                for item in split1:
                    if not '.' in item:
                        l = item.replace(" ", "")
                        lot.append(l)

        i = 0
        checked2 = list(checked)
        checked2.pop()
        checked = tuple((checked2))

        points = []
        while not i == len(checked):
            for item in citys:
                if str(checked[i]) in item:
                    h = item.split(":")
                    for item3 in h:
                        if "." in item3:
                            points.append(item3)
            i = i + 1

        for cord in points:
            c,b = cord.split(",")
            cordsin = ()
            ci = float(c)
            bi = float(b)
            print(cord)
            folium.Circle(location=[c, b], popup=f"Possible Player Location", fill_color=f"red", radius=200000, weight=2, color=f"red").add_to(testmap)



        testmap.save('index.html')
