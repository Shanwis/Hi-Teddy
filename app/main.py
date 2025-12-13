from config import BUFFER_SIZE
from recognizer import recognizer, stream, porcupine
from commands import commands
from nlu import detect_intent
from single_instance import set_instance,cleanup
from tts import speak
import json
import struct

set_instance()
print("Teddy is running now.....")
speak("Hello, for my assistance just say the magic phrase")

while True:
    frame = stream.read(porcupine.frame_length, exception_on_overflow=False)
    pcm = struct.unpack_from("h" * porcupine.frame_length, frame)

    if porcupine.process(pcm) >= 0:
        speak("Yes?")
        print("Teddy is listening.....")

        while True:
            data = stream.read(BUFFER_SIZE, exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                command = result["text"].strip().lower()

                print("Command:",command)        
                intent = detect_intent(command)

                if(intent in commands.keys()):
                    speak(f"Executing {intent.replace('_',' ')}")
                    commands[intent]()
                    break
                elif(intent == 'cancel'):
                    speak("Ok, cancelled.")
                    break
                else:
                    speak("Listening.")
