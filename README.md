# 🗣️ Text to Speech Desktop App (Python)

A simple and elegant **Text to Speech (TTS)** desktop application built using **Python** and **Tkinter**. This app allows users to enter text, select a language, and convert the input into spoken audio using the `pyttsx3` text-to-speech engine.

---

## ✅ Features

- Text-to-speech conversion for English, French, and Arabic (based on available system voices)
- Modern and responsive GUI
- Dropdown menu to choose the speech language
- Clean, user-friendly design
- Offline functionality — no internet connection required

---

## 🛠️ Requirements

Ensure you have **Python 3** installed. Then, install the required library:

```bash
pip install pyttsx3
```

> **Note:** Voice support for French and Arabic depends on available voices on your system (Windows/macOS/Linux). Additional voices may need to be installed manually.

---

## ▶️ How to Run

1. Save the script as `text_to_speech.py`.
2. Open a terminal or command prompt in the script directory.
3. Run:

```bash
python text_to_speech.py
```

---

## 🧠 How It Works

1. Enter your desired text into the text box.
2. Select a language (English, French, or Arabic).
3. Click the **Convert** button.
4. The application reads the text aloud using a system voice that matches the selected language.

---

## 📦 Technologies Used

- Python
- Tkinter (GUI)
- pyttsx3 (Text-to-Speech)

---

## 📌 GUI Overview

| Element             | Description                          |
|---------------------|--------------------------------------|
| Text Box            | Input area for typing or pasting text |
| Language Dropdown   | Choose between English, French, Arabic |
| Convert Button      | Converts text to speech              |

---

## ⚠️ Notes

- Voice language support depends on your system. If the selected voice isn't available, the app will fall back to the default system voice.
- Arabic and French may not work properly unless specific TTS voices are installed.

---

## 📄 License

This project is open-source and free to use for personal or educational purposes.

---

## ✨ Future Improvements

- Add voice rate and volume controls
- Support for saving speech to audio files (e.g., MP3)
- Auto-detect text language
