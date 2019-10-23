import speech_recognition as sr
import keyboard
from HelperFunctions import listMicrophones

r = sr.Recognizer()
#listMicrophones()
while True:
    with sr.Microphone(device_index=1) as source:
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")