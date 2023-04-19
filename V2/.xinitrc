[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

###Start applications before qtile
nm-applet &
blueman-applet &
dunst &
picom &
#amixer sset Master unmute &

###Start Doom Emacs daemon/server
/usr/bin/emacs --daemon &

exec qtile start
