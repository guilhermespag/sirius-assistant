
#!/usr/bin/env python3
import os
import speech_recognition as sr
from gtts import gTTS
import time

def speak(text):
    tts = gTTS(text=text, lang='pt')
    tts.save("voices/voz.mp3")
    os.system('termux-media-player play voices/voz.mp3')

def check_bluetooth():
    status = os.popen('termux-bt').read()
    if "connected:true" in status:
        speak("JBL conectada. Assistente Sirius pronto.")
        return True
    else:
        speak("JBL não conectada. Verifique a conexão Bluetooth.")
        return False

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='pt-BR').lower()
        return command
    except:
        return ""

def set_volume(level):
    os.system(f"termux-volume music {level}")

def get_volume():
    vol = os.popen('termux-volume music').read()
    return vol.strip()

# Inicialização
if not check_bluetooth():
    exit()

speak("Diga Sirius para começar")

while True:
    command = listen()
    if "sirius" in command:
        speak("Estou ouvindo")
        command = listen()

        if "aumenta" in command or "aumentar" in command:
            set_volume(10)
            speak("Volume aumentado.")
        elif "abaixa" in command or "diminuir" in command:
            set_volume(3)
            speak("Volume reduzido.")
        elif "qual o volume" in command or "volume atual" in command:
            volume = get_volume()
            speak(f"O volume atual é {volume}.")
        elif "desligar" in command or "encerrar" in command:
            speak("Encerrando o assistente. Até mais.")
            break
        else:
            speak("Comando não reconhecido.")
