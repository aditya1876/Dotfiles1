import os

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from libqtile.widget import clock

import functions
#import clock

# Colors
colors = {
    "rosewater"   : "#f4dbd6",
    "flamingo"    : "#f0c6c6",
    "pink"        : "#f5bde6",
    "mauve"       : "#c6a0f6",
    "red"         : "#ed8796",
    "maroon"      : "#ee99a0",
    "peach"       : "#f5a97f",
    "yellow"      : "#eed49f",
    "green"       : "#a6da95",
    "teal"        : "#8bd5ca",
    "sky"         : "#91d7e3",
    "sapphire"    : "#7dc4e4",
    "blue"        : "#8aadf4",
    "lavender"    : "#b7bdf8",
    "text"        : "#cad3f5",
    "subtext1"    : "#b8c0e0",
    "subtext0"    : "#a5adcb",
    "overlay2"    : "#939ab7",
    "overlay1"    : "#8087a2",
    "overlay0"    : "#6e738d",
    "surface2"    : "#5b6078",
    "surface1"    : "#494d64",
    "surface0"    : "#363a4f",
    "base"        : "#24273a",
    "mantle"      : "#1e2030",
    "crust"       : "#181926"
}

##Mod Keys
mod='mod4'

##Applications
MyTerminal = 'alacritty'
MyBrowser = 'vieb'
MyCodeEditor = 'code'
MyBrowser2 = 'firefox -p "main"'
MyCalculator = 'speedcrunch'
MyMusicPlayer = 'elisa'
MyFileManager = 'thunar'
MyTextEditor = 'notepadqq'
MyEmacsClient = 'emacsclient -c -a "emacs"'
MyLauncher = 'rofi -show drun'
MyScratchTextEditor = 'mousepad /home/adi/02_Docs/my_scratchpad.md'

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc = "Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc = "Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc = "Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc = "Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc = "Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc = "Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc = "Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc = "Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc = "Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc = "Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc = "Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc = "Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc = "Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc = "Toggle fullscreen"),
    Key([mod, "control"], "f", lazy.window.toggle_floating(), desc = "Toggle floating"),
    
#     # Toggle between split and unsplit sides of stack.
#     # Split = all windows displayed
#     # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
#     Key([mod, "shift"], "Space", lazy.layout.toggle_split(), desc = "Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Space", lazy.next_layout(), desc = "Toggle between layouts"),
    
    # Close windows
    Key([mod], "q", lazy.window.kill(), desc = "Kill focused window"),

    # Qtile Management
    Key([mod, "control"], "b", lazy.hide_show_bar(), desc = "Toggle Show Hide Qtile Bar"),
    Key([mod, "control"], "r", lazy.reload_config(), desc = "Reload qtile config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc = "Shutdown Qtile"),

    #Applications
    Key([mod], "t", lazy.spawn(MyTerminal), desc = "Launch terminal"),
    Key([mod], "z", lazy.spawn(MyBrowser), desc = "Launch vieb browser"),
    Key([mod], "x", lazy.spawn(MyCodeEditor), desc = "Launch vs code"),
    Key([mod], "c", lazy.spawn(MyCalculator), desc = "Launch speedcrunch"),
    Key([mod], "b", lazy.spawn(MyBrowser2), desc = "Launch firefox 'main' profile"),
    Key([mod], "n", lazy.spawn(MyEmacsClient), desc = "Launch emacs client"),
    Key([mod], "w", lazy.spawn(MyTextEditor), desc = "Launch notepadqq"),
    Key([mod], "e", lazy.spawn(MyFileManager), desc = "Launch thunar"),
    Key([mod], "r", lazy.spawn(MyLauncher), desc = "Launch rofi - apps"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show window"), desc = "Launch rofi - windows"),
    Key([mod], "l", lazy.spawn("betterlockscreen -l"), desc = "Lock screen using betterlockscreen"),

    # Hardware/system control
    #Sound
    Key([], "XF86AudioMute", lazy.spawn("pamixer toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

    #Music
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),

    #Screenlocking
    Key([mod], "l", lazy.spawn("betterlockscreen -l"), desc = "Lock the screen"),

    # Emacs programs launched using the key chord CTRL+e followed by 'key'
    # KeyChord([mod],"a", [
    #     Key([], "e",lazy.spawn("emacsclient -c -a 'emacs'"),desc='Emacsclient Dashboard'),
    #     Key([], "a",lazy.spawn("emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/05_Music/\")'"),desc='Emacsclient EMMS (music)'),
    #     Key([], "b",lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),desc='Emacsclient Ibuffer'),
    #     Key([], "d",lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),desc='Emacsclient Dired'),
    #     Key([], "i",lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),desc='Emacsclient ERC (IRC)'),
    #     Key([], "n",lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),desc='Emacsclient Elfeed (RSS)'),
    #     Key([], "s",lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),desc='Emacsclient Eshell'),
    #     Key([], "v",lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),desc='Emacsclient Vterm'),
    #     Key([], "w",lazy.spawn("emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"),desc='Emacsclient EWW Browser')
    # ]),


]

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label="ﴬ"),
    Group("5", label=""),
    Group("6", label="")
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle = True), desc="Switch to group {}".format(i.name),),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="Switch to & move focused window to group {}".format(i.name),),
        ])

## Scratchpads
# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('MyTerminal', MyTerminal, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('MyScratchTextEditor', MyScratchTextEditor, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    #DropDown('MyTextEditor', MyTextEditor, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('MyFileManager', MyFileManager, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('MyTerminal')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('MyScratchTextEditor')),
    #Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('MyTextEditor')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('MyFileManager')),
])

##Layouts
layouts = [
    layout.Columns(border_focus = colors["sapphire"], border_normal = colors["base"], margin = 2, border_width = 1,),
    layout.MonadTall(border_focus = colors["sapphire"], border_normal = colors["base"], margin = 2, border_width = 1,),
    layout.MonadWide(border_focus = colors["sapphire"], border_normal = colors["base"], margin = 2, border_width = 1,),
    layout.Floating(border_focus = colors["sapphire"], border_normal = colors["base"], margin = 2, border_width = 1,),
    #layout.Spiral(border_focus = colors["sapphire"], border_normal = colors["base"], margin = 6, border_width = 1,),
    #layout.Max(),
    #layout.Bsp(),
    layout.Matrix(border_focus = colors["sapphire"], border_normal = colors["base"], margin = 6, border_width = 1,),
    #layout.RatioTile(),
    #layout.Tile(),
    layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(fontsize=20, margin_y=3, margin_x=4, borderwidth=1, active=colors["sky"],block_highlight_text_color=colors["rosewater"],
                inactive=colors["overlay0"], rounded=True, disable_drag=True,highlight_method='line',invert=True,rainbow=True),
                widget.TextBox(offset=-1, padding=1, text = '',),
                widget.Image(filename='~/.config/qtile/assets/bar/cpu.png',margin=3),         
                widget.CPU(format = '{load_percent:.0f}% ',padding=-1),
                widget.Image(filename='~/.config/qtile/assets/bar/ram.png',margin=2),         
                widget.Memory(format = '{MemUsed: .0f}{mm} ',padding = -1,),
                widget.Image(filename='~/.config/qtile/assets/bar/hdd.png',margin=2),         
                widget.DF(format = '{f} GB',padding = 0,partition = '/home',visible_on_warn=False,),
                widget.Spacer(length=bar.STRETCH,),
                widget.WindowName(format='{name}',max_chars=60,),
                widget.Image(filename='~/.config/qtile/assets/bar/vol3.png',margin=2,),
                widget.GenPollText(func=functions.fn_volume_value, update_interval=0.1, padding=-1,),
                widget.Image(filename='~/.config/qtile/assets/bar/sun.png', margin=2,),
                widget.GenPollText(func=functions.fn_brightness_value,update_interval=0.1,padding=-1,),
                widget.Image(filename='~/.config/qtile/assets/bar/battery.png',margin=2),
                widget.Battery(charge_char='',discharge_char='',format='{char}{percent:2.0%} ',padding=-1,),
                widget.Image(filename='~/.config/qtile/assets/bar/bluetooth.png',margin=2),         
                widget.GenPollText(func=functions.fn_bluetooth_name,update_interval=5,padding=-1,),
                widget.Image(filename='~/.config/qtile/assets/bar/wifi.png',margin=2),
                widget.GenPollText(func=functions.fn_wifi_name,update_interval=5,padding=-1,),
                widget.TextBox(offset=-1, padding=1, text = '',),
                #qtile.call_later(1,functions.fn_capslock()), 
                functions.fn_capslock(), #function to display if capslock on or off
                functions.fn_numlock(), #function to display if numlock on or off
                widget.TextBox(offset=-1, padding=1, text = '',),
                widget.Image(filename='~/.config/qtile/assets/bar/clock.png',margin=1),
                widget.Clock(format='%a, %b %d - %H:%M:%S ',long_format = '%b %-d, %Y',padding = 1,),         
                widget.CurrentLayoutIcon(padding=0,scale=0.9,custom_icon_paths=[os.path.expanduser("~/.config/qtile/assets/layout/"),],),
            ],
            22,
            margin=[3, 3, 3, 3],
            opacity=0.8,
            background=colors["base"]
        ),
        #Random wallpaper everytime config is loaded (folder = ~/Wallpapers)
        wallpaper = str(functions.fn_randomWallpaper()),
        wallpaper_mode='fill'
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

