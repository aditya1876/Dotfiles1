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
    - root password = Same as user password
    - user acccount = create new user > yes to sudo access
    - profile = minimal
    - audio = pipewire
    - kernels = choose only zen kernel
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

### Create a swap file -- recheck this
```
sudo dd if=/dev/zero of=/swapfile bs=1M status=progress count=2048 #chagne count value for different swapsize
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
- sudo pacman -Syu

### Installing yay
- git clone https://aur.archlinux.org/yay.git
- cd yay_dir
- makepkg -si

### Copy your repo from github
- copy all files to local in proper directories
```
#git clone git@github.com:aditya1876/Dotfiles1.git #this does not work without .ssh folder
git clone https://github.com/aditya1876/Dotfiles1.git
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
- sudo systemctl enable ufw

### Changing systemwide themes
- qt5ct
    - append the following to `/etc/environment` file
    ```
    QT_QPA_PLATFORMTHEME="qt5ct"
    ```
- set look and feel
    - xfconf-query -c xsettings -p /Net/ThemeName -s "Adwaita-dark"
    - xfconf-query -c xsettings -p /Net/IconThemeName -s "Adwaita-dark"
    - gsettings set org.gnome.desktop.interface gtk-theme "Adwaita-dark"
    - gsettings set org.gnome.desktop.interface icon-theme "Adwaita-dark"

### Restart into Qtile

### Firefox
    - copy .mofilla/firefox form external hdd (backup_secrets) to ~/mozilla/firefox
    - Launch firefox with profile > about:profiles > delete the profile named 'default' > create a new profile named 'default' > make this profile as default 

### VS code
    - Turn on Setting sync in profile icon and login using github profile
    - create a new .ssh key and save in .ssh/
        - `ssh-keygen -t ed25519 -C "your_github_Email"`
        - Enter (default location= ~/.ssh)
        - Enter passphrase
        - check public and private key created in .ssh/
        - `eval $(ssh-agent -s)`
        - `ssh-add ~/.ssh/Private_key` (id_XXXX)
        - Add public key to github
            - `cat ~/.ssh/public_key` (id_xxx.pub)
            - copy the entire output
            - go to github.com > your icon > settings>access> ssh and gpg keys > Add new > give any title > paste public key

### Copy data from external Hard Disk 
    - backup folder

### Mousepad
    - Setup mousepad after new install
        - Copy 02_docs from backup
        - View > colour scheme > cobalt
        - view > check line numbers
        - view > uncheck menu bar (use alt to display menubar)
        - view > font > fira code > size 12

### Miniconda
- download latest linux version from website
- run 'bash filename'
- select yes to all questions during install

### DOOM Emacs
- install doom emacs from the github page - https://github.com/doomemacs/doomemacs

    
## TODO
- [] How to turn off laptop screen when external monitor is connected
- [] Update capslock and Numlock indicator on the fly
- [] Copy doomemacs config to repo
- [] Learn Photo mangement with feh, vimiv or find photo management tool
