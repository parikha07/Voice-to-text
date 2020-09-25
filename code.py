#This library needs an active Internet connection to work

pip install speechrecognition

#To accept the input in audio format from the default microphone
pip install pyaudio

import speech_recognition as SGR
import time

#storing audio input
store=SGR.Recognizer()

with SGR.Microphone() as s:
    print("Speak....")
    
    audio_input = store.record(s, duration=10)
    #record() accepts the voice from usser and upload it to the recognition engine
    #duration is taken 10 seconds here
    
    print("Recording Time: ", time.strftime("%I:%M:%S"))
    
    try:
        text_output= store.recognize_google(audio_input)
        print("Text converted from audio: \n")
        print(text_output)
        print("Finished!!")
    except:
        print("Couldn't process the audio input")
        
        
