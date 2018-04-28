import speech_recognition as sr

def speech_to_text():
    config = {
        "url": "https://stream.watsonplatform.net/speech-to-text/api",
        "username": "f15abd3a-3703-4f7e-8967-cc2a2ad4e5ab",
        "password": "j4e3PFrUHbGK"
    }
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        audio = r.listen(source,phrase_time_limit=5)  # read the entire audio file
    # Signup for IBM watson here https://www.ibm.com/watson/ and get the username and password.
    IBM_USERNAME = config[
        'username']  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = config['password']  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        print('processing')
        text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        print(f'{text}')
        return text
    except sr.UnknownValueError:
        text = "IBM Speech to Text could not understand audio"
        print(text)
        return text
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))
        return e
