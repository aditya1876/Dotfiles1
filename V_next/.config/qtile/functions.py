from libqtile import widget
import os, subprocess, random
from subprocess import check_output
import time

#function to get volume value
def fn_volume_value() -> str:
    my_cmd="pamixer --get-volume"
    output = subprocess.Popen(my_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    output=output.decode()[:-1] #convert byte to str and remove last\n char
    return output

#function to get bluetooth connected device name
def fn_bluetooth_name() -> str:
    my_cmd="bluetoothctl info | grep 'Name:' | cut -d : -f 2 | awk '{$1=$1};1'"
    output = subprocess.Popen(my_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    output=output.decode()[:-1] #convert byte to str and remove last\n char
    return output

#function to get the brightness value
def fn_brightness_value() -> str:
    my_cmd = "brightnessctl info | grep 'Current brightness:' | cut -d : -f 2 | cut -d ' ' -f 3 |tr -d '(' | tr -d ')'"
    output = subprocess.Popen(my_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    output=output.decode()[:-1] #convert byte to str and remove last \n char
    return output

#function to get the Wifi network name
def fn_wifi_name() -> str:
    #my_cmd = "nmcli connection show | grep 'wifi'| cut -d ' ' -f 1"
    my_cmd = "nmcli connection show | sed -n '2 p' | cut -d ' ' -f 1"
    output = subprocess.Popen(my_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    output=output.decode()[:-1] #convert byte to str and remove last \n char
    return output

#Function to display if Capslock is on or off
def fn_capslock():# -> widget:
    my_cmd = "xset q | grep Caps | cut -d : -f 3| awk '{$1=$1};1' | cut -d ' ' -f 1" 
    output = subprocess.Popen(my_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    output=output.decode()[:-1] #convert byte to str and remove last \n char
    if output=='off':
        return widget.Image(filename='~/.config/qtile/assets/bar/capsOff.png',margin=2)
    elif output=='on':
        return widget.Image(filename='~/.config/qtile/assets/bar/capsOn.png',margin=2)

#Function to display if numlock is on or off
def fn_numlock():# -> widget:
    my_cmd = "xset q | grep Num | cut -d : -f 5 | awk '{$1=$1};1' | cut -d ' ' -f 1"
    output = subprocess.Popen(my_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    output=output.decode()[:-1] #convert byte to str and remove last \n char        
    if output=='off':
        return widget.Image(filename='~/.config/qtile/assets/bar/numOff.png',margin=2)
    elif output=='on':
        return widget.Image(filename='~/.config/qtile/assets/bar/numOn.png',margin=2)

#Function to select a wallpaper randomly
def fn_randomWallpaper():
    wallpaper_dir='/home/adi/Wallpapers/'
    #print(wallpaper_dir+random.choice(os.listdir(wallpaper_dir)))
    #print(type(random.choice(os.listdir(wallpaper_dir))))
    return wallpaper_dir + random.choice(os.listdir(wallpaper_dir))
