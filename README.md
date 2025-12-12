# Hey Teddy : A buddy for system voice assistance

This is a project attempting to make an offline voice assistant using the vosk library for voice-to-text parsing. I want to have an extensive selection of commands which can be executed through voice.

## Features (of V1)

Teddy can support the following commands:

### System control
* Shutdown
* Reboot
* Logout
* Lock screen

### Application control
* open terminal
* open browser
* open VS Code

### Window control
* close active window
    * Works only for xorg/xwayland windows currently

### Audio control
* Mute/Unmute speakers
* Increase/Decrease volume

### Brightness control
* Increase/Decrease brightness

### Network control
* Turn Wi-Fi on/off
* Turn bluetooth on/off

### Battery status
* Says the battery level out loud

## Working

### Wake Word + Offline Speech Recognition

Teddy listens for a wake word using:

**Porcupine (Picovoice)** — highly accurate wake-word engine

**Vosk (vosk-model-small-en-us-0.15)** — low-memory offline speech-to-text model ideal for command recognition

No cloud processing. No internet required.

## Project structure

```bash
Hey-Teddy/
├── models/
│   └── vosk-model-small-en-us-0.15/
├── app
│   ├── commands.py
│   ├── config.py
│   ├── main.py
│   ├── nlu.py
│   ├── recognizer.py
│   └── tts.py
├── Requirements
│   ├── linux_requirements.txt
│   └── requirements_python.txt
├── .gitignore
├── LICENSE
└── README.md

```

## Installation
1. Clone the repo

```bash
git clone https://github.com/<your-username>/Hi-Teddy.git
cd Hi-Teddy
```

2. Install dependencies
```bash
pip install -r Requirements/Requirements/requirements_python.txt
sudo dnf install wmctrl brightnessctl nmcli
```

3. Download Vosk model

```bash
Place the following model in the models/ folder:
vosk-model-small-en-us-0.15
```

4. Run Teddy

```bash
python app/main.py
```

## Why Teddy?

It is quite nice to have a friendly companion in you laptop or desktop. It gives it a certain personality. 

Teddy is not meant to compete with online cloud assistants. It is a offline, extendable buddy.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Notes & Limitations
* Close Window

    close_window only works for Xorg / XWayland windows using wmctrl.
    Wayland-native apps cannot be closed externally due to GNOME security restrictions.

* Microphone Must Be Active

    Vosk requires continuous access to the microphone.
    If the mic is blocked by permissions or another app, Teddy will not hear commands.

