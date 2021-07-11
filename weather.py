import os 
import time 

os.system(' clear ')
A = str(input(" if you are new please type -i ==>>  "))

if 'i' in A:
       os.system(' pip install python-weather ')
else:
    os.system(' clear ')
    print(" Running weather! ") 
    time.sleep(2)  


import os
import python_weather
import sys 

os.system(' clear ')
print(" ___________________________")
print("|EX: Los Angeles California|")
print("|__________________________|")
print("| automation for weather   |")
print("==================================")
weather = str(input(" Living Area ==>>  "))
print("==================================")

os.system(f' weather {weather} ')

time.sleep(2)
print("|==================|")
print("|Have a nice one :D|")
print("|==================|")
sys.exit()