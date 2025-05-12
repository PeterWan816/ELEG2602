import speech_recognition as sr
import threading

assistant_name = 'luck'
listener = sr.Recognizer()

# Shared variable to signal when to stop monitoring
stop_Speaking = True
stop_monitoring = False


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
                else:
                    continue

        except sr.UnknownValueError:
            print('You didn’t say anything or Unable to recognize your speech.')

        except sr.RequestError as e:
            print('Error occurred during speech recognition:', str(e))