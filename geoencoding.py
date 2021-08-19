import requests
import time
import os

imgs = os.listdir("./data")
cwd = os.getcwd()
count = 0

for image in imgs:
    if "DS" not in image:
        coords = image[:len(image) - 4]
        split_coords = coords.split(",")
        lat = float(split_coords[0])
        lng = float(split_coords[1])
        request_url = "https://nominatim.openstreetmap.org/reverse?lat={}&lon={}&format=json&zoom=3&email=tobias.wirtz1@gmail.com".format(lat, lng)
        r = requests.get(request_url)
        res = r.json()
        if 'address' in res: 
            cc = res['address']['country_code']
            path = '/labeled_data/' + cc
            folder = cwd + path
            if os.path.isdir(folder):
                old_fp = cwd + '/data/' + image
                new_fp = folder + '/' + image
                os.rename(old_fp, new_fp)
            else:
                os.mkdir(folder)
                old_fp = cwd + '/data/' + image
                new_fp = folder + '/' + image
                os.rename(old_fp, new_fp)
    time.sleep(1) 
    count += 1
    print(count)
