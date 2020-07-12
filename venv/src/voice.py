from gtts import gTTS
import os

def start_voice(name):
    mytext = 'Welcome' + name

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome

    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("welcome.mp3")