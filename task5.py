from gtts import gTTS
from pygame import time, mixer


import speech_recognition as sr
import threading

assistant_name = 'luck'
listener = sr.Recognizer()

# Shared variable to signal when to stop monitoring
stop_Speaking = True
stop_monitoring = False

def speak(command) :
    tts = gTTS(command, lang='en-us')
    tts.save("output.mp3")

    # Initialize the pygame.mixer module
    mixer.init()

    # Load the audio file using pygame.mixer.music.load()
    mixer.music.load("output.mp3")

    # Play the audio file using pygame.mixer.music.play()
    mixer.music.play()

    # Give pygame enough time to load and start playing the audio.
    while mixer.music.get_busy():
        pass

    # Cleanup the loading of file
    mixer.quit()
speak(assistant_name.upper() + ' is ready, your majesty!')
# Shared variable to signal when to stop monitoring
def monitor_audio(source):
    # Continuously monitor the audio while it's being received
    silent = True
    while not stop_monitoring:
        try:
            with sr.Microphone() as monitor:
                # Listen to a short segment of audio to check if speech is present
                audio = listener.listen(monitor, phrase_time_limit=0.5)
                if audio:
                    if silent:
                        silent = False
                        print(">> listening ...", end="")
                    else:
                        print(" ...", end="")
        except KeyboardInterrupt:
            break


while True:
    if stop_Speaking:
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)

                print("\n[" + assistant_name.upper() + ' is ready, your majesty!]')

                # Create a separate thread to monitor the audio
                stop_monitoring = False
                audio_thread = threading.Thread(target=monitor_audio, args=(source,))
                audio_thread.start()

                # Listen for the user's speech
                voice = listener.listen(source)

                # Stop monitoring thread
                stop_monitoring = True

                if voice:
                    print("\n")
                    translated_voice = listener.recognize_google(voice).lower()
                    print('You said: "' + translated_voice + '".')
                    if assistant_name.lower() in translated_voice:

                        # Find the index of assistant_name in translatedVoice
                        index = translated_voice.lower().index(assistant_name.lower())

                        # Extract the text after assistant_name
                        command = translated_voice[index + len(assistant_name):].strip()

                        if 'play' in command:
                            song = command[command.index('play'):].strip()

                            speak("Got it, I'll help you to " + song + ', your majesty!')

                            pywhatkit.playonyt(song)
                    speak('You said: "' + translated_voice + '".')
                else:
                    continue

        except sr.UnknownValueError:
            print('You didn’t say anything or Unable to recognize your speech.')

        except sr.RequestError as e:
            print('Error occurred during speech recognition:', str(e))