""" adapted from javascript by http://no.nonsense.ee/qthmap/
"""

import android, time, os, math
def returnQth(lat, lng):
  qth = '' 
  lat += 90 
  lng += 180
  lat = lat / 10 + 0.0000001
  lng = lng / 20 + 0.0000001
  qth += chr(65 + lng) + chr(65 + lat)
  lat = 10 * (lat - math.floor(lat))
  lng = 10 * (lng - math.floor(lng))
  qth += chr(48 + lng) + chr(48 + lat)
  lat = 24 * (lat - math.floor(lat))
  lng = 24 * (lng - math.floor(lng))
  qth += chr(65 + lng) + chr(65 + lat)
  lat = 10 * (lat - math.floor(lat))
  lng = 10 * (lng - math.floor(lng))
  qth += chr(48 + lng) + chr(48 + lat)
  lat = 24 * (lat - math.floor(lat))
  lng = 24 * (lng - math.floor(lng))
  qth += chr(65 + lng) + chr(65 + lat)
  return qth

droid = android.Android()
droid.startLocating()
loc = droid.readLocation()
while not loc[1].has_key('gps') :
    print("Waiting for GPS lock")
    time.sleep(2)
    loc = droid.readLocation()
f = open('/sdcard/sl4a/scripts/logfile.txt','w')
f.write('altitude, latitude, longitude, QTH \n')
f.close()
count = 0
while True:
    loc = droid.readLocation()
    count = count + 1
    alt = str(loc.result['gps']['altitude'])
    lat = str(loc.result['gps']['latitude'])
    lon = str(loc.result['gps']['longitude'])
    grid = returnQth(lat, lon)
    f = open('/sdcard/sl4a/scripts/logfile.txt','a')
    f.write(alt + ',' + lat + ',' + lon + ',' + grid  '\n')
    print(str(count) + ',' + alt + ',' + lat + ',' + lon + ',' + grid  '\n')
    f.close()
    time.sleep(5)