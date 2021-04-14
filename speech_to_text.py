import speech_recognition as SRG 
import time
import speech
import json

def speech_to_text(src):
    store = SRG.Recognizer()
    print("Text recognizing...")
    print(src)
    with SRG.Microphone() as s: 
        audio_input = store.record(s, duration=2)
        # text_output = store.recognize_google(audio_input, language=src)
        # return text_output
        try:
            text_output = store.recognize_google(audio_input, language=src)
            return text_output
            #return 
        except:
            response=json.dumps({"error": "Couldn't process the audio input."})
            return response

# src="en"
# speech_to_text(src)

# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     recognizer.adjust_for_ambient_noise(source, duration=1)
#     print("Recording for 4 seconds")
#     recorded_audio = recognizer.listen(source, timeout=4)
#     print("Done recording")

# try:
#     text = recognizer.recognize_google(recorded_audio, language="en-US")
#     print(text)
# except Exception as ex:
#     print(ex)