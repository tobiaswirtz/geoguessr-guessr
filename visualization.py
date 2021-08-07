import plotly.graph_objects as go
import os
import pandas as pd

placeNames = os.listdir("./data")
d = {"lat": [], "lng": []}
for name in placeNames:
    arr = name.split(",")
    lat = float(arr[0])
    lng = float((arr[1])[:len(arr[1])-4])
    d["lat"].append(lat)
    d["lng"].append(lng)

df = pd.DataFrame(d)

fig = go.Figure(data=go.Scattergeo(
        lon = df['lng'],
        lat = df['lat'],
        mode = 'markers',
        ))

fig.update_layout(
        title =  '765 Collected Data Points Aug 7th'
    )
fig.show()
