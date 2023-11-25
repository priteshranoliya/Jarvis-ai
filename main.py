import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import numpy as np
import requests

def get_weather(api_key, city):
    weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
    try:
        data = weather_data.json()
        if weather_data.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return "Unable to fetch weather information."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def say(text):
    os.system(f'say "{text}"')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Hello Pritesh this is Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"],
                 ["netflix", "https://www.netflix.com"], ["github", "https://www.github.com"],
                 ["amazon", "https://www.amazon.com"],
                 ["twitter", "https://www.twitter.com"],
                 ["reddit", "https://www.reddit.com"],
                 ["linkedin", "https://www.linkedin.com"],
                 ["instagram", "https://www.instagram.com"],
                 ["stackoverflow", "https://stackoverflow.com"],
                 ["spotify", "https://www.spotify.com"],
                 ["ebay", "https://www.ebay.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            sec = datetime.datetime.now().strftime("%S")
            say(f"Sir time is {hour} hours {min} minutes {sec} seconds")

        elif "what is weather".lower() in query.lower():
            openweathermap_api_key = "33b9f921430e2b0824626cf253e879ae"

            say("Sir please enter the city name: ")
            city = input("Enter the city name: ")
            weather_info = get_weather(openweathermap_api_key, city)
            print(weather_info)
            say(weather_info)

        elif "open facetime".lower() in query.lower():
            say(f"Opening facetime sir...")
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open whatsapp".lower() in query.lower():
            say(f"Opening whatsapp sir...")
            os.system(f"open /Applications/WhatsApp 2.app")

        elif "open safari".lower() in query.lower():
            say(f"Opening safari sir...")
            os.system(f"open  / Applications / Safari.app")

        elif "open mail".lower() in query.lower():
            say(f"Opening mail sir...")
            os.system(f"open  /System/Applications/Mail.app")

        elif "open vs code".lower() in query.lower():
            say(f"Opening code editor sir...")
            os.system(f"open  /Applications/Visual Studio Code.app")

        elif "open apple TV".lower() in query.lower():
            say(f"Opening apple TV sir...")
            os.system(f"open  /System/Applications/TV.app")

        elif "open prime video".lower() in query.lower():
            say(f"Opening prime video sir...")
            os.system(f"open  /Applications/Prime Video.app")

        elif "Jarvis Quit".lower() in query.lower():
            print("Quitting")
            say("signing off....")
            exit()

        elif "Thanks JARVIS".lower() in query.lower():
            say("Welcome Pritesh....")

        # say(query)
