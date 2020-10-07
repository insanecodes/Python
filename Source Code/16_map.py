# Python program to open map in web browser
import folium
import webbrowser
import os


# Map method of folium return Map object 
# Here we pass coordinates 
geo= folium.Map(location=[28.457523,77.026344])


# save method of Map object will create a map
geo.save('index.html')


#Open html file in web browser
webbrowser.open('file://' + os.path.realpath('index.html'))