import subprocess
import re
import requests
import folium
import webbrowser
from selenium import webdriver 
import time 
driver = webdriver.Chrome() 
 
url = "file:///path\\to\\file\\map.html"

driver.get(url) 
# location=(20.5937, 78.9629),zoom_start=7
m = folium.Map()
locc = []



def add_to_map(loc,ip):
    if len(locc) == 0 or len(locc) == 1:
        folium.Marker(loc,popup = f' Router {ip}',icon=folium.Icon(color='green')).add_to(m)

    else:
        folium.Marker(loc,popup = f' Router {ip}').add_to(m)
    if len(locc) > 1:
        folium.PolyLine(locations = locc,line_opacity = 0.5).add_to(m)
    m.save("map.html")
    print("refresh")
    driver.refresh()

# folium.Marker([21.1524499,79.1166237],popup = ' baddiestore ').add_to(m)

def get_loc(ip,first):
    try:
        if ip == "192.168.0.1":
            da = requests.get(f"http://ip-api.com/json/")
        else:
            da = requests.get(f"http://ip-api.com/json/{ip}")
    except:
        return
    if da.json()["status"] != "fail":
        print(da.json())
        gh = (da.json()["lat"],da.json()["lon"])
        if not first:
            locc.append(gh)
        print(len(locc))
        add_to_map(gh,ip)

try:
    process = subprocess.Popen(["tracert", "guiamais.com.br"],stdout=subprocess.PIPE, text=True)
    print(process.stdout)

    des_ip = None

    for line in process.stdout:
        # print(line)
        if "* * *" in line:
            continue
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
        if match:
            if des_ip == None:
                des_ip = match.group(1)
                get_loc(des_ip,True)
                # process.terminate()
                # break
            else:
                print(match.group(1))
                get_loc(match.group(1),False)  # Print only the IP

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")

print(locc)

time.sleep(60)
