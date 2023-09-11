import folium
import pandas as pd
import webbrowser
webbrowser.open('https://www.python.org')

#DEPLOY MAP
mapa = folium.Map(location=[4.0638178,-76.5205],
                  zoom_start=12)

mapa.save('expenses/index.html')
webbrowser.open('expenses/index.html')

