import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import random

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speaking speed
engine.setProperty('volume', 1.0)  # Volume level

# Predefined phrases
# phrases = {
#     "greet": ["Hi there!", "Hello, friend!", "Let's learn something fun!"],
#     "praise": ["Great job!", "You're a superstar!", "Wow! That was smart!"],
#     "encourage": ["Try again!", "Almost there!", "You can do it!"],
#     "bye": ["See you later!", "Goodbye!", "Come back soon!"]
# }

# Speak function
def speak(text):
    chat_log.insert(tk.END, "Bot: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

# Listen to the microphone
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            query = recognizer.recognize_google(audio)
            chat_log.insert(tk.END, "You: " + query + "\n")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I can't connect to the speech service.")
            return ""

# Get a number from voice
def get_number(prompt):
    speak(prompt)
    number_text = listen()
    try:
        return int(number_text)
    except:
        speak("That's not a number. Try again.")
        return None

# Command processor
def process_command():
    command = listen()

    if "hello" in command:
        speak(random.choice(phrases["greet"]))
    elif "your name" in command:
        speak("I'm Miko Buddy. I help with your studies.")
    elif "add" in command or "plus" in command:
        num1 = get_number("Say the first number.")
        num2 = get_number("Say the second number.")
        if num1 is not None and num2 is not None:
            result = num1 + num2
            speak(f"{num1} plus {num2} is {result}. {random.choice(phrases['praise'])}")
    elif "bye" in command:
        speak(random.choice(phrases["bye"]))
        root.quit()
    elif "count" in command:
        speak("Let's count from 1 to 5!")
        speak("1, 2, 3, 4, 5")
        speak(random.choice(phrases["praise"]))
    elif "animal" in command:
        speak("A cow says moo! A dog says woof! An owl says hoot hoot!")
    else:
        speak("I'm still learning. Try asking something else!")

# GUI window
root = tk.Tk()
root.title("Kids AI – Miko Buddy")
root.geometry("500x400")
root.config(bg="#FFEBB7")

# Title
title = tk.Label(root, text="🤖 Miko Buddy – Study Assistant", font=("Comic Sans MS", 16, "bold"), bg="#FFEBB7")
title.pack(pady=10)

# Chat area
chat_log = tk.Text(root, height=15, width=60, font=("Arial", 12))
chat_log.pack(pady=5)

# Button
listen_button = tk.Button(root, text="🎤 Speak Now", font=("Comic Sans MS", 14), bg="#FF7B54", fg="white", command=process_command)
listen_button.pack(pady=10)

# Start app
speak("Hello! I'm your learning friend. Press the button and talk to me!")
root.mainloop()
