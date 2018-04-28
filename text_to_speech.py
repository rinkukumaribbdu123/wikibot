from gtts import gTTS
import os


def speak_content(data):
    tts = gTTS(text= data, lang='en')
    tts.save("temp.mp3")
    import pyglet
    music = pyglet.resource.media('temp.mp3')
    music.play()
    pyglet.app.run()

