#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

#Launch picom on startup
#picom &

#unmute on start
#amixer sset Master unmute

######DOOM EMACS########
#start doom emacs daemon/ server at user login
#/usr/bin/emacs --daemon &
########################

###Start Xserver when user logs in#####
if systemctl -q is-active graphical.target && [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec startx
fi
#######################
