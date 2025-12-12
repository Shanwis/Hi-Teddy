from vosk import Model, KaldiRecognizer
import pvporcupine
from config import SAMPLE_RATE
import pyaudio
from dotenv import load_dotenv
import os

load_dotenv()
PORCUPINE_KEY = os.getenv("PICOVOICE_ACCESS_KEY")
if not PORCUPINE_KEY:
    raise RuntimeError("PICOVOICE_ACCESS_KEY not set")

porcupine = pvporcupine.create(access_key=PORCUPINE_KEY,keyword_paths=["models/Hey-Teddy_en_linux_v3_0_0.ppn"])
model = Model(r"models/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model,SAMPLE_RATE, '["open", "terminal", "browser", "shutdown", "reboot", "lock", "screen", "cancel", "close", "window", "speaker", "up", "down","increase","decrease","volume","mute","unmute","speaker", "brightness", "battery", "power", "level", "internet", "on", "off", "bluetooth","reduce", "editor"]')

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, input=True, frames_per_buffer=8192)

stream.start_stream()