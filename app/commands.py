import os
from tts import speak

def battery():
    percent = open("/sys/class/power_supply/BAT0/capacity").read().strip()
    speak(f"battery level is {percent}%")

commands = {
    "shutdown":lambda:os.system("shutdown now"),
    "reboot":lambda:os.system("reboot"),
    "logout":lambda:os.system("gnome-session-quit --logout --no-prompt"),
    "lock": lambda:os.system("loginctl lock-session"),

    "open_terminal":lambda:os.system("gnome-terminal"),
    "open_browser":lambda: os.system("brave-browser"),
    "close_window":lambda: os.system("wmctrl -c :ACTIVE:"),

    "mute_speaker":lambda: os.system("pactl set-sink-mute @DEFAULT_SINK@ true"),
    "unmute_speaker":lambda: os.system("pactl set-sink-mute @DEFAULT_SINK@ false"),
    "volume_up":lambda: os.system("pactl set-sink-volume @DEFAULT_SINK@ +10%"),
    "volume_down":lambda: os.system("pactl set-sink-volume @DEFAULT_SINK@ -10%"),

    "brightness_up":lambda: os.system("brightnessctl set +10%"),
    "brightness_down":lambda: os.system("brightnessctl set 10%-"),

    "wifi_off":lambda:os.system("nmcli radio wifi off"),
    "wifi_on":lambda:os.system("nmcli radio wifi on"),
    
    "bluetooth_on":lambda:os.system("bluetoothctl power on"),
    "bluetooth_off":lambda:os.system("bluetoothctl power off"),
    
    "battery_status":battery
}