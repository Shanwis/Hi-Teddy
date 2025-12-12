INTENTS = {
    "shutdown": ["shutdown", "power off", "turn off"],
    "reboot": ["reboot", "restart"],
    "logout": ["log out", "sign out"],
    "lock": ["lock screen", "lock"],

    "open_terminal": ["open terminal", "launch terminal"],
    "open_browser":["open browser", "launch browser"],
    "open_editor":["open editor", "launch editor"],
    "close_window":["close window","stop window"],

    "mute_speaker":["mute speaker"],
    "unmute_speaker":["unmute speaker"],
    "volume_up":["increase volume","volume up"],
    "volume_down":["decrease volume", "reduce volume","volume down"],

    "brightness_up":["increase brightness", "brightness up"],
    "brightness_down":["decrease brightness", "reduce brightness","brightness down"],

    "wifi_off":["internet off", "stop internet"],
    "wifi_on":["internet on"],

    "bluetooth_off":["bluetooth off", "stop bluetooth"],
    "bluetooth_on":["bluetooth on"],

    "battery_status":["battery level","power level", "battery"],

    "cancel": ["cancel", "stop", "nevermind"]
}

def detect_intent(text):
    text = text.lower()

    for intent, phrases in INTENTS.items():
        for phrase in phrases:
            if phrase in text:
                return intent
    return None