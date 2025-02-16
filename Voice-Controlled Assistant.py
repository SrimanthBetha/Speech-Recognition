import speech_recognition as sr
import webbrowser
import os
import subprocess

r = sr.Recognizer()

def record_text():
    print("Listening for input...")
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source, timeout=5)
            print("Audio received, processing...")

            MyText = r.recognize_google(audio)
            print(f"Recognized Text: {MyText}")
            return MyText.lower()  # Convert to lowercase for easier matching
            
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio. Please repeat.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None

def execute_command(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        print("Opening Google...")
        print("What do you want to search for on Google?")
        search_query = record_text()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            print(f"Searching for {search_query} on Google...")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        print("Opening YouTube...")
        print("What do you want to play on YouTube?")
        song_name = record_text()
        if song_name:
            webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
            print(f"Playing {song_name} on YouTube...")
    # Add more elif clauses as needed
    elif "exit" in command or "quit" in command:
        print("Goodbye!")
        return True
    else:
        print("Sorry, I didn’t recognize that command. Please try again.")
    return False

while True:
    text = record_text()
    if text:
        if execute_command(text):
            break  # Exit the loop if "exit" or "quit" command is detected
