import tkinter as tk
from tkinter import *
import pyttsx3

# Initialize the main application window
app = Tk()

# Configure the appearance of the main window
app.title("Text To Speech")
app.geometry("500x500")
app.configure(bg="#f0f8ff")
app.resizable(0, 0)

# Create a LabelFrame with a border and a background color
obj = LabelFrame(app, text="Text To Speech", font=("Arial", 16, "bold"), bd=2, bg="#e6f7ff", padx=10, pady=10)
obj.pack(fill="both", expand="yes", padx=20, pady=20)

# Label for text entry
lbl = Label(obj, text="Enter Text:", font=("Arial", 14, "bold"), bg="#e6f7ff")
lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Text widget for user input
txt = Text(obj, width=45, height=10, font=("Arial", 12), wrap=WORD, bg="#ffffff", bd=2, relief=SUNKEN)
txt.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Label for language selection
lang_lbl = Label(obj, text="Select Language:", font=("Arial", 14, "bold"), bg="#e6f7ff")
lang_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Language options
languages = ["English", "French", "Arabic"]
selected_language = StringVar(value=languages[0])

# Dropdown menu for language selection
lang_menu = OptionMenu(obj, selected_language, *languages)
lang_menu.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Function to convert text to speech
def convert_text_to_speech():
    text = txt.get("1.0", END).strip()
    lang = selected_language.get()
    
    if text:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        # Map languages to voice names based on available voices
        voice_map = {
            "English": "english",
            "French": "french",
            "Arabic": "arabic"
        }
        
        lang_voice = voice_map.get(lang, "english")
        voice_found = False
        
        for voice in voices:
            if lang_voice in voice.name.lower() or lang_voice in voice.languages:
                engine.setProperty('voice', voice.id)
                voice_found = True
                break
        
        if not voice_found:
            engine.setProperty('voice', voices[0].id)  # Fallback to default voice if not found
        
        engine.say(text)
        engine.runAndWait()

# Button to trigger text-to-speech conversion
btn = Button(app, text="Convert", font=("Arial", 14, "bold"), command=convert_text_to_speech, bg="#4caf50", fg="#ffffff", relief=RAISED)
btn.pack(padx=20, pady=20)

# Run the application
app.mainloop()
