# My Arch Dotfiles

## General Instructions
* Look at the Todo, make some improvements and create a V4 folder to add latest/updated configs

### Install base minimal arch
- Insert and start bootable USB
- connect to internet
```
iwctl
station wlan0 show
station wlan0 scan
station wlan0 connect <SSID> <Enter> <enter password>
quit
ping google.com - CTRL+C
```
- pacman-key --init
- pacman-key --populate archlinux
- archinstall
    - mirror list = australia (search using /)
    - local langauage = en_GB.UTF-8
    - Drives = select using tab
    - disk layout = select option to wipe and autosetup - ext4 - yes (/home)
    - disk encryption = set lan password (script giving error if not provided)
    - swap = no (create swapfile later)
    - hostname = adimc01 / adimc02
    - root password = <no change>
    - user acccount = create new user > yes to sudo access
    - profile = minimal
    - audio = pipewire
    - kernels = <no change>
    - Additional packages = git vim xf86-video-intel or xf86-video-amdgpu(install rest of the packages using packageslist files later)
    - Network Config = NetwrokManager
    - Timezone = Asia/Kolkata
    - Optional Repo = Multilib
- Install
- Would you like to chroot into newly created installation and perform post-installation configurations? = NO
- Reboot (remove usb)
- Login using newly created user
- nmcli device wifi connect <SSID> password <Password>
- ping google.com

### Wifi Powersave
- create file = `/etc/NetworkManager/conf.d/wifi-powersave.conf` and add following
```
[connection]
wifi.powersave = 2
``` 
- sudo systemctl restart NetworkManager

### Create a swap file
```
sudo dd if=/dev/zero of=/swapfilebs=1M status=progress count=2048 #chagne count value for different swapsize
#the above command makes the swapfile

sudo chmod 600 /swapfile
sudo mkswap -U clear /swapfile #copy the swapfile info displayed
#launch tty `alt+ctrl+F2`
#login
sudo su -
echo '/swapfile none swap defaults 0 0/swapfile' | tee -a /etc/fstab
cat /etc/fstab #check the addition
reboot now #restat and check swap addition
free -h #check if swap is running
```

### System update
- sudo pacman -S archlinux-keyring
- sudo pacman -Syu

### Installing yay
- git clone <git url from archlinux yay page>
- cd yay_dir
- makepkg -si

### Copy your repo from github
```
git clone <repo>
mkdir ~/.config/ (if not existing)
cp -r <repo>/.config/* ~/.config/
cp <repo>/.bash_profile ~/.bash_profile (check if anything existing alreay)
cp <repo/.bashrc ~/.bashrc (check if already existing)
mkdir ~/Wallpapers
cp -r <repo>/Wallpapers/* ~/Wallpaper/
```

### Install packages from package lists
- sudo pacman -S $(cat PackageList.txt)
- yay -S $(catAUR_PackageList.txt)

### Start services
- sudo systemctl enable --now bluetooth.service
- sudo systemctl enable sddm
- sudo systemctl enable ufw

### Changing systemwide themes
- qt5ct
    - append the following to `/etc/environment` file
    ```
    QT_QPA_PLATFORMTHEME="qt5ct"
    ```
- copy sddm theme
    - sudo cp -R sdt /usr/share/sddm/themes/
    - sudo chown -R $USER:$USER /usr/share/sddm/themes/sdt
    - sudo mkdir /etc/sddm.conf.d
    - touch /etc/sddm.conf.d/10.theme.conf
    ```
    [Theme]
    Current=sdt
    ```
- set look and feel
    - xfconf-query -c xsettings -p /Net/ThemeName -s "Adwaita-dark"
    - xfconf-query -c xsettings -p /Net/IconThemeName -s "Adwaita-dark"
    - gsettings set org.gnome.desktop.interface gtk-theme "Adwaita-dark"
    - gsettings set org.gnome.desktop.interface icon-theme "Adwaita-dark"

### DOOM Emacs
- `sudo pacman -S git emacs ripgrep fd` #should have been installed as part of packagelist.txt
- install doom emacs from the github page
- update .bashrc #should be part of the copied .bashrc file
```
#add emacs to path
export PATH="$PATH:$HOME/.emacs.d/bin"

#alias to start emacs client after the deamon has been started in .bash_profile
alias emacs = "emacsclient -c -a 'emacs' &"
```
- update .bash_profile to start emacs daemon at startup
```
#inside .bash_profile
#start emacs daemon at user login
/usr/bin/emacs --daemon
```

### Set up github keys

### Miniconda
- download tat.gz from anaconda website and run 'bash filename'
- select yes to all questions during install

### brave
- sync in settings
### VS code
    - Sync using 'setting sync'

## TODO
- [] How to turn off laptop screen when external monitor is connected
- [] Update capslock and Numlock indicator on the fly
- [] Copy doomemacs config to repo
- [] Learn Photo mangement with feh, vimiv or find photo management tool
- [] where to keep the brave and vscode sync data
