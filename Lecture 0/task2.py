from gtts import gTTS
from pygame import time, mixer

stop_Speaking = False
# Convert text to speech using gtts and save it as an audio file
command = " Nice to meet you dummy!"
tts = gTTS(command, lang='en-us')
tts.save("output.mp3")

# Initialize the pygame.mixer module
mixer.init()

# Load the audio file using pygame.mixer.music.load()
mixer.music.load("output.mp3")

# Play the audio file using pygame.mixer.music.play()
mixer.music.play()

#Give pygame enough time to load and start playing the audio.
while mixer.music.get_busy():
 pass

# Cleanup the loading of file
mixer.quit()
stop_Speaking = True