#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

#Launch picom on startup
picom &

#unmute on start
amixer sset Master unmute

######DOOM EMACS########
#start doom emacs daemon/ server at user login
/usr/bin/emacs --daemon &
########################
