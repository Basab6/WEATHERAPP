import requests
import json
import pyttsx3
from datetime import date

def get_detail(city,time):
    url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{time}?key=RRK59Z7Z3RUSMLNRUJB49BX2H"
    r=requests.get(url)
    dic=json.loads(r.text)

    x1=dic["address"]
    x2=dic["latitude"]
    x3=dic["longitude"]
    x4=dic["days"][0]["datetime"]
    x5=dic["days"][0]["tempmin"]
    x6=dic["days"][0]["tempmax"]
    x7=dic["days"][0]["temp"]
    x8=dic["days"][0]["conditions"]
    x9=dic["days"][0]["description"]
    
    report=(f"The address is {x1}\n"
    f"The latitude is {x2}\n"
    f"The longitude is {x3}\n"
    f"The datetime is {x4}\n"
    f"The min-temperature is {x5}\n"
    f"The max temperature is {x6}\n"
    f"The temperature is {x7}\n"
    f"The conditions are {x8}\n"
    f"The description is {x9}\n") 
     # a report string

    print(report)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    #for i, voice in enumerate(voices):
       # print(f"Voice {i}: {voice.name}, ID: {voice.id}")

    # Try a different voice
    engine.setProperty('voice', voices[9].id)  # or try voices[11].id

    engine.say(report)
    engine.runAndWait()
if __name__=="__main__":
    city=input("Enter city details\n")
    time=date.today()
    print(f"Getting information on date:{time}")
    get_detail(city,time)