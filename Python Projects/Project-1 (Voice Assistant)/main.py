import speech_recognition as sr
import pyttsx3
import webbrowser
import requests

from AppOpener import open, close
from songs import songLibraries
from openai import OpenAI


# def aiProcess(command):
#     client = OpenAI(
#         api_key="",
#     )

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
#             },
#             {
#                 "role": "user",
#                 "content": "Compose a poem that explains the concept of recursion in programming.",
#             },
#         ],
#     )

#     print(completion.choices[0].message.content)



def speak(text):
    engine = pyttsx3.init()  # object creation
    """ RATE"""
    engine.setProperty("rate", 180)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty("volume")
    engine.setProperty("volume", 0.8)  # setting up volume level between 0 and 1

    """VOICE"""
    voices = engine.getProperty("voices")
    engine.setProperty(
        "voice", voices[1].id
    )  # changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()
    
    
def openCloseApplication(command):
    if "open" in command.lower():
        words = command.lower().split(" ")
        app = words[1]
        open(app, match_closest=True)
        speak(f"Opening {app}.")
    
    elif "close" in command.lower():
        words = command.lower().split(" ")
        app = words[1]
        close(app, match_closest=True, output=False)
        speak(f"Closing {app}.")


def commandExecution(command):
    if "google" in command.lower():
        webbrowser.open("https://www.google.com")

    elif "youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")

    elif "facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")

    elif "instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")

    elif "linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")

    elif "github" in command.lower():
        webbrowser.open("https://www.github.com")

    elif "open" in command.lower() or "close" in command.lower():
        openCloseApplication(command)

    elif command.lower().startswith("play"):
        words = command.lower().split(" ")
        words.remove("play")
        song = "_".join(words)
        link = songLibraries[song.lower()]
        webbrowser.open(link)
    
    # elif "news" in command.lower():
    #     api_key = ""
    #     response = requests.get(
    #         f"https://newsapi.org/v2/everything?q=tesla&from=2024-06-03&sortBy=publishedAt&apiKey={api_key}"
    #     )
    #     if response.status_code == 200:
    #         news_data = response.json()
    #         for article in news_data['articles']:
    #             speak(f"Title: {article['title']}")
    #             speak(f"Description: {article['description']}")
    #     else:
    #         print(f"Failed to retrieve news: {response.status_code}")

    else:
        # aiProcess(commmand)
        speak(f"Sorry, I didn't understand the command {command}.")


def main():
    recognizer = sr.Recognizer()
    print("Say something!")

    while True:
        try:
            print("Listening...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                command_text = recognizer.recognize_google(audio)
                print(command_text)

            if "jarvis" in command_text.lower():
                speak("Yes sir!")
                print("Jarvis is active, listening for your command...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print("Command received:", command)
                    commandExecution(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
