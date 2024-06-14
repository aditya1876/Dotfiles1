#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

########EXPORTS#########
export HISTCONTROL=ignoredups:erasedups           # no duplicate entries

########SETTINGS########

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"


########
#ALCI
########
#alias evb='sudo systemctl enable --now vboxservice.service'  ---delete this line if you dont see any problems in usage

#########ALIAS##########
alias ls='ls -lact --color=auto'
alias em="emacsclient -c -a 'emacs' &" #doomemacs client mode
alias n="nvim"
alias fm="ranger"
alias grep="grep --color=auto"

# git
alias gs="git status"
alias ga="git add ."
alias gc="git commit -m"
alias gph="git push origin"
alias gpu="git pull origin"

#mount and unmount usb(only works for 1 usb at a time. will fail if 2 usbs are connnected)
#alias mount_it="udisksctl mount -b /dev/sdb1" 
#alias unmount_it="udisksctl unmount -b /dev/sdb1"
alias mount_it="sudo mount /dev/sdb1 /run/media/adi/MyPassport"
alias unmount_it="sudo umount -l /dev/sdb1"

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

#Switch to external monitor
alias switch="xrandr --output HDMI-1 --mode 1920x1080"

#Searching thourgh history for a command
#run - 'his git' to search for all git commands in history
function his(){
  history | grep "$1";
}
#########################

##########PROMPTS##########
#PS1='[\u@\h \W]\$ '

#PS1="\[$(tput bold)$(tput setab 6)$(tput setaf 7)\]\u@\h|\W|\t >>>\[$(tput sgr0)\]"
#change the values of setab and setaf between 1-7 to change the colour of the foreground and background
#Colourful prompt
FMT_BOLD="\[\e[1m\]"
FMT_DIM="\[\e[2m\]"
FMT_RESET="\[\e[0m\]"
FMT_UNBOLD="\[\e[22m\]"
FMT_UNDIM="\[\e[22m\]"
FG_BLACK="\[\e[30m\]"
FG_BLUE="\[\e[34m\]"
FG_CYAN="\[\e[36m\]"
FG_GREEN="\[\e[32m\]"
FG_YELLOW="\[\e[33m\]"
FG_GREY="\[\e[37m\]"
FG_MAGENTA="\[\e[35m\]"
FG_RED="\[\e[31m\]"
FG_WHITE="\[\e[97m\]"
BG_BLACK="\[\e[40m\]"
BG_BLUE="\[\e[44m\]"
BG_CYAN="\[\e[46m\]"
BG_GREEN="\[\e[42m\]"
BG_YELLOW="\[\e[43m\]"
BG_MAGENTA="\[\e[45m\]"

###Calculating command timer###
function timer_now {
    date +%s%N
}

function timer_start {
    timer_start=${timer_start:-$(timer_now)}
}

function timer_stop {
    local delta_us=$((($(timer_now) - $timer_start) / 1000))
    local us=$((delta_us % 1000))
    local ms=$(((delta_us / 1000) % 1000))
    local s=$(((delta_us / 1000000) % 60))
    local m=$(((delta_us / 60000000) % 60))
    local h=$((delta_us / 3600000000))
    # Goal: always show around 3 digits of accuracy
    if ((h > 0)); then timer_show=${h}h${m}m
    elif ((m > 0)); then timer_show=${m}m${s}s
    elif ((s >= 10)); then timer_show=${s}.$((ms / 100))s
    elif ((s > 0)); then timer_show=${s}.$(printf %03d $ms)s
    elif ((ms >= 100)); then timer_show=${ms}ms
    elif ((ms > 0)); then timer_show=${ms}.$((us / 100))ms
    else timer_show=${us}us
    fi
    unset timer_start
}

###Function for displaying git branch###
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'
}

###Function for Creating the Prompt###
set_prompt(){
    PS1="${FG_BLUE}╭─${FMT_RESET}" # begin arrow to prompt
    PS1+="${BG_MAGENTA}${FG_CYAN}${FMT_BOLD}  ${FG_WHITE}\u ${FMT_RESET}" # OS and user
    PS1+="${BG_BLUE}${FG_WHITE}${FMT_BOLD} \w ${FMT_RESET}" # DIRECTORY container
    PS1+="${BG_CYAN}${FG_GREY}${FMT_BOLD} " #Files container
    PS1+=" \$(find . -mindepth 1 -maxdepth 1 -type d | wc -l) " # number of folders
    PS1+=" \$(find . -mindepth 1 -maxdepth 1 -type f | wc -l) " # number of files
    PS1+=" \$(find . -mindepth 1 -maxdepth 1 -type l | wc -l) " # number of symlinks
    PS1+="${FMT_RESET}"
    PS1+="${BG_GREEN}${FG_WHITE}${FMT_BOLD}  \t ${FMT_RESET}" # Time container
    PS1+="${BG_YELLOW}${FMT_BOLD}${FG_GREY}  $(parse_git_branch) ${FMT_RESET}" # Git container
    timer_stop
    PS1+="${BG_BLACK}${FG_GREY}${FMT_BOLD} 󰔟 $timer_show ${FMT_RESET}" # Time container
    PS1+="\n${FG_BLUE}╰ ${FMT_RESET}" # end arrow to prompt
}

###Display the prompt###
trap 'timer_start' DEBUG
PROMPT_COMMAND='set_prompt'

#########################################

#########BASH-COMPLETION##########
if [ -f /etc/bash_completion ]; then
  source /etc/bash_completion
fi
##################################

##########DOOM EMACS##############
#export PATH="$PATH:$HOME/.emacs.d/bin"
export PATH="$PATH:$HOME/.config/emacs/bin"
###################################

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/adi/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/adi/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/adi/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/adi/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


PATH=~/.console-ninja/.bin:$PATH
