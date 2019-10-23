import speech_recognition as sr
from HelperFunctions import listMicrophones

r = sr.Recognizer()
listMicrophones()
while True:
    with sr.Microphone(device_index=1) as source:
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=8)
        try:
            with open(r"C:\Users\Dexter\Downloads\hardsoftapplication-52182c5dd661.json", "r") as f:
                credentials = f.read()
            text = r.recognize_google_cloud(audio, credentials_json= credentials)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")