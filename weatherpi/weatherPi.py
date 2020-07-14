import time
import os, sys
import csv
from sense_hat import SenseHat

from bs4 import BeautifulSoup
import requests
from datetime import datetime

sys.path.insert(0,'/home/pi/weatherPi/')
from weatherpi.sunny import sunAnimation
from weatherpi.cloudy import cloudAnimation
from weatherpi.rainy import rainAnimation
from weatherpi.snowy import snowAnimation
from weatherpi.thunder import thunderAnimation

#Configuration of display-------------------------------

#Brightness control. Max of 1
BRIGHTNESS = 0.4

#Displayed Pixel will be red if above RED_TEMP. It will transition to blue as the temp aproaches BLUE_TEM$
#Below BLUE_TEMP, pixel will be white (Usually indicating freezing)
RED_TEMP = 40.0
BLUE_TEMP = 0.0
#-------------------------------------------------------

sense = SenseHat()

#Get time and weather----------------------------------
cTime = time.localtime()
cTemp = sense.get_temperature()
cPres = sense.get_pressure()
cHumi = sense.get_humidity()

cDatetime = str(datetime.now())
#Get conditions
soup = BeautifulSoup(requests.get("https://weather.com/weather/today/l/a620a61ecfab914ca71b8b470703a7e2d913180d5b13298f3d251c61d76fd985").content,"html.parser")
cConditions = soup.find("div",{'data-testid':'wxPhrase'}).text


#------------------------------------------------------

print("Current temperature: {} C".format(cTemp))

#Record weather---------------------------------------------

fileName= '/home/pi/weatherPi/weather_data/'+str(cTime[0])+'_weatherData.csv'

if os.path.exists(fileName):
    with open(fileName,'a',newline='') as f:
        writ = csv.writer(f)
        writ.writerow([cDatetime,cTemp,cPres,cHumi,cConditions])
else:
    with open(fileName,'w',newline='') as f:
        writ = csv.writer(f)
        writ.writerow(['Datetime','Temperature','Pressure','Humidity','Conditions'])
        writ.writerow([cDatetime,cTemp,cPres,cHumi,cConditions])
#-------------------------------------------------------------

#Display on Matrix--------------------------------------------

sense.set_rotation(90,redraw=False)
#sunAnimation(sense)
#cloudAnimation(sense)
#rainAnimation(sense)
#snowAnimation(sense)
#thunderAnimation(sense)

#If it is the first of the month, reset all pixels
if cTime[2]==1 and cTime[3]==0 and cTime[4]==0:
    #first minute of new month
    sense.clear()
    #rotating the matrix properly
    sense.low_light = False

#12:00 pm - display temperature
if (cTime[3]==12 and cTime[4]==0):

    rgbVal = [0,0,0]
    if cTemp <=BLUE_TEMP:
        rgbVal = [int(255*BRIGHTNESS),int(255*BRIGHTNESS),int(255*BRIGHTNESS)]
    elif cTemp>=RED_TEMP:
        rgbVal = [int(255*BRIGHTNESS),0,0]
    else:
        #The percent of the way between RED_TEMP and BLUE_TEMP
        tPerc = (cTemp-BLUE_TEMP)/(RED_TEMP-BLUE_TEMP)
        rgbVal = [int(x*BRIGHTNESS) for x in [255*tPerc,0,255*(1-tPerc)]]
    
    #print("color is {}".format(rgbVal))
    
    #Find next available pixel
    cDay = (cTime[6]+1)%7
    for i in range(int((cTime[2]-1)/7),8):
        if sense.get_pixel(cDay,i)==[0,0,0]:
            sense.set_pixel(cDay,i,tuple(rgbVal))
            break
    
