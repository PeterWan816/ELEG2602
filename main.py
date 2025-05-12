from gtts import gTTS

# Convert text to speech
text = "丢雷楼某!"
tts = gTTS(text, lang='en')

# Save the speech as an audio file
tts.save("output.mp3")