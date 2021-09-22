# Import the required module for text to speech conversion
from typing import Text
from gtts import gTTS

# This module is imported so that we can play the converted audio
import os

# The text that you want to convert to audio
mytext = 'I shall conquer this world '

# Google search result for the text you want to convert to audio
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = mytext

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	print(j)

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# Sound
myobj.save("Sound.mp3")

# Playing the converted file
os.system("Sound.mp3")