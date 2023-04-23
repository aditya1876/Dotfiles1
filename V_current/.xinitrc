[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

###Start applications before qtile
nm-applet &
blueman-applet &
dunst &
picom &

###Start Doom Emacs daemon/server
/usr/bin/emacs --daemon &

#start qtile session now
qtile start
