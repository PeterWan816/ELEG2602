from gtts import gTTS
from pygame import time, mixer

import pywhatkit
import csv
import wikipedia
import datetime
import pyjokes
import os
import speech_recognition as sr
import threading

assistant_name = 'Lucy'
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
                        elif 'search' in command:
                            item = command.replace('search', '')
                            info = wikipedia.summary(item, 1)
                            print(info)
                            speak(info)
                        elif 'time' in command:
                            time = datetime.datetime.now().strftime('%I:%M %p')
                            speak('Current time is ' + time)
                        elif 'are you single' in command:
                            NumOfCompanion = 3
                            speak('I’ve got ' + str(NumOfCompanion) + ' relationship before.')
                        elif 'joke' in command:
                            speak(pyjokes.get_joke())
                        elif 'name' in command:
                            speak("My name is" + assistant_name)
                        elif 'whatsapp my mother' in command:
                            Target = 'Mother'
                            PhoneNumber = '+85212345678'
                            Msg = 'Not going home to eat!\nYou eat yourself?'
                            pywhatkit.sendwhatmsg_instantly(PhoneNumber, Msg, 10, True, 3)
                            print(f"Message sent to {Target} with Phone Number {PhoneNumber}:\n>> {Msg}")
                            speak(f"Message sent to {Target} with Phone Number {PhoneNumber}: {Msg}")
                        elif 'whatsapp image' in command:
                            Target = 'Mother'
                            PhoneNumber = "+85212345678"
                            # Specify the relative path to the image
                            image_path = "images/funny.jpg" # Ensure this path is correct
                            caption = "Hi " + Target + "\n\n" + "Relax!\nYou feel better now?"
                            # Check if the image file exists before sending
                            if os.path.isfile(image_path):
                                try:
                                    # Send the image with the caption
                                    pywhatkit.sendwhats_image(PhoneNumber, image_path, caption, 8, True, 3)
                                    print(f"Message sent to {Target} with Phone Number {PhoneNumber}:\n>> {caption}")
                                    speak(f"Message sent to {Target} with Phone Number {PhoneNumber}:\n>> {caption}")
                                except Exception as e:
                                    print(f"An error occurred: {e}")
                            else:
                                print(f"Image not found: {image_path}")
                        elif 'whatsapp my schedule' in command:
                            with open("send_msg.csv", "r", encoding='utf-8') as file:
                                reader = csv.DictReader(file) # Use tab as delimiter
                                for row in reader:
                                    # Create the full message including the greeting
                                    message = 'Hi ' + row['Recipient'] + ',\n\n' + row['Message'].replace('\\n', '\n')
                                    phone = row['Phone']
                                    image_path = row['ImagePath']
                                    print(row) # Print the row for debugging
                                    # Check if ImagePath is not empty
                                    if image_path:
                                    # Ensure the image file exists before sending
                                        if os.path.isfile(image_path):
                                            pywhatkit.sendwhats_image(phone, image_path, message, 8, True, 3)
                                        else:
                                            print(f"Image not found: {image_path}")
                                    else:
                                        pywhatkit.sendwhatmsg_instantly(phone, message, 8, True, 3)
                                speak("All messages have been sent")
                        else:
                            speak('I heard you your majesty! But I am unclear about your instruction. Could you please repeat it')
                    speak('You said: "' + translated_voice + '".')
            
                else:
                    continue

        except sr.UnknownValueError:
            print('You didn’t say anything or Unable to recognize your speech.')

        except sr.RequestError as e:
            print('Error occurred during speech recognition:', str(e))
