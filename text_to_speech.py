from gtts import gTTS
import os
textInput = input('')
language = 'en'
output = gTTS(text = textInput, lang = language, slow = False)
output.save("audio.mp3")
os.system("start audio.mp3")
