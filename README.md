# geo-traceroute

Get the location of every hop of packet in the map.
this is just a demo which uses traceroute and tracert.



![image](https://raw.githubusercontent.com/gromaxbro/geo-traceroute/refs/heads/main/Screenshot%202025-02-09%20165757.png)


## installation
`pip install folium selenium`

## change the things specific to os
windows : `process = subprocess.Popen(["tracert", "{website}"],stdout=subprocess.PIPE, text=True)`
linux :  `process = subprocess.Popen(["traceroute","-n", "{website}"],stdout=subprocess.PIPE, text=True)`
