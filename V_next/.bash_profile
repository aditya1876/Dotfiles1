#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

###Start Xserver when user logs in#####
if systemctl -q is-active graphical.target && [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec startx
fi
#######################
