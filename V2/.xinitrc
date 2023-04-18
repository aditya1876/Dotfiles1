[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
nm-applet &
blueman-applet &
dunst &

exec qtile start
