import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess
from playsound import playsound
import wolframalpha
import requests
import time


print('Loading your computer assistant - Bimex')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')
engine.setProperty("rate", 130)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def beginning():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,good morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,good afternoon")
        print("Hello,good afternoon")
    else:
        speak("Hello,good evening")
        print("Hello,good evening")


def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-us')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Please repeat again...")
            return "None,"
        return statement


speak("im Bimex your computer assistant")
beginning()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you ?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if 'hello' in statement:
            speak('hi Dear user')
            print('hi Dear user')

        if 'bye' in statement or 'goodbye' in statement:
            speak('Are you satisfied with my performance?')
            answer = takeCommand()
            if 'yes' in answer:
                speak('thank you, I hope I was able to help you.')

            elif 'no' in answer:
                speak("I'm so sorry, I'm trying to get better in the future.")

            speak('your personal assistant Bimex is shutting down,Good bye')
            print('your personal assistant Bimex is shutting down,Good bye')
            break

        elif 'how are you' in statement:
            speak('fine,I hope I can help you as well as any other advanced robot')
            speak('and how are you, Sir')
            print('fine,I hope I can help you as well as any other advanced robot')
            request = takeCommand()
            if 'fine' in request or 'good' in request:
                speak("It's good to know that your fine")

        elif 'what can you do' in statement:
            speak('I am Bimex your persoanl assistant.I am programmed to minor tasks like opening wikipedia,youtube'
                  'google chrome,gmail,amazon,your IDE and predict time,predict weather in different cities,play music,'
                  'write the text you want and show it ,search ,talk about siri ,Show location ,world News,some information'
                  'about me and my creator, you can ask me computational or geographical questions too! and ect')

        elif 'what is your name' in statement:
            speak("im Bimex your computer assistant ")
            print("im Bimex your computer assistant ")

        elif 'who made you' in statement or 'who created you' in statement:
            speak("I was built by miss Rahmani and she is a computer engineering student")
            print("I was built by miss Rahmani and she is a computer engineering student")

        elif 'who am I' in statement:
            speak("If you talk then definately your human")
            print("If you talk then definately your human")

        elif 'siri' in statement:
            speak("who is siri? i am the best")
            print("who is siri? i am the best")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open wikipedia' in statement or 'wikipedia' in statement:
            webbrowser.open_new_tab("https://www.wikipedia.org/")
            speak("wikipedia is open now")
            time.sleep(5)

        elif 'open youtube' in statement or 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement or 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open amazon' in statement:
            speak("Amazon is open now")
            webbrowser.open_new_tab("https://www.amazon.com")
            time.sleep(5)

        elif 'open gmail' in statement or 'gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Gmail is open now")
            time.sleep(5)

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
            speak('Here are some new news about the countries of the world')
            time.sleep(5)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            speak("tell me what do you want to find?")
            time.sleep(5)

        elif 'take note' in statement or 'take' in statement:
            speak("ok what should I write?")
            f = open('my_file.txt', 'a+')
            f.write(takeCommand())
            f.close()

        elif 'show note' in statement or 'show' in statement:
            speak("Showing note")
            old_file = open(r'my_file.txt', 'r')
            speak(old_file.read())

        elif 'Visual Studio' in statement or 'V S code' in statement or 'usual' in statement:
            command = r"G:\vsc\Microsoft VS Code\Code.exe"
            subprocess.Popen(command)
            speak("visual studio is open now")
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak("City Not Found")

        elif 'location' in statement:
            speak("Google map is open now")
            webbrowser.open_new_tab("https://www.google.com/maps/@29.6390276,52.5241672,18z?hl=fa")
            time.sleep(6)

        elif 'play music' in statement or 'music' in statement or 'play' in statement:
            speak("music is play now")
            playsound('Conor Maynard- Someone You Loved.mp3')
            speak('Okay, here is your music! Enjoy!')
            time.sleep(6)

        elif 'log off' in statement or 'sign out' in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        else:
            fi = open('unknown_commands.txt', 'w+')
            fi.write(takeCommand())
            speak("dear user i'm so sorry ")
            speak("but your command was unknown fore me.")
            fi.close()

time.sleep(3)
