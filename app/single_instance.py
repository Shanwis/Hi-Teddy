import os
import sys
import atexit

LOCKFILE="/tmp/hey_teddy.lock"

def set_instance():
    if os.path.exists(LOCKFILE):
        from tts import speak
        speak("Hey, one instance is already running")
        sys.exit(0)
    
    with open(LOCKFILE,"w") as f:
        f.write(str(os.getpid()))

    atexit.register(cleanup)

def cleanup():
    if os.path.exists(LOCKFILE):
        os.remove(LOCKFILE)