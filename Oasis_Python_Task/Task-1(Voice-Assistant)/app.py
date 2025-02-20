import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")
        return ""

def timer(seconds):
    speak(f"Starting a {seconds} second timer.")
    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining")
        time.sleep(1)
    speak("Time's up!")

def main():
    speak("Hello! How can I help you today?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hi there! How can I assist you?")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif "search" in command:
            speak("What do you want to search for?")
            query = listen()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Here are the results for {query}")
        elif "timer" in command:
            speak("For how many seconds?")
            try:
                seconds = int(listen())
                timer(seconds)
            except ValueError:
                speak("I didn't catch that. Please say a number.")
        elif "what is your name" in command:
            speak("I am your voice assistant! You can call me whatever you like.")
        elif "how are you" in command:
            speak("I'm just a program, but thanks for asking! How can I help you today?")
        elif "tell me a joke" in command:
            speak("Why don’t skeletons fight each other? They don’t have the guts!")
        elif "what is the weather" in command:
            speak("I'm not connected to a weather API right now, but you can check online for the latest weather update!")
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
