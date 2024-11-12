import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener = sr.Recognizer()

speaker = pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
speaker.setProperty('rate', 150)     # setting up new voice rate

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


def speak(text):
    speaker.say('yes boss,' +text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

va_name = 'Whale'

speak_ex('I am your ' + va_name + ', Tell me sir.')

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')
                #print(command)
                #speak(command)

    except:
         print('check your Microphone')
    return command
while True:
    user_command = take_command()
    if 'close' in user_command:
        print('see you again boss. I will be there when ever you call me.')
        speak('see you again boss. I will be there when ever you call me.')
        break
    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
    elif 'play' in user_command:
        user_command = user_command.replace('play ', '')
        print('playing ' + user_command)
        speak('playing ' + user_command + ', enjoy boss.')
        pk.playonyt(user_command)
        break
    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for ', '')
        user_command = user_command.replace('google ', '')
        speak('searching for' + user_command)
        pk.search(user_command)
    
    elif 'who is' in user_command:

        user_command = user_command.replace('who is ', '')
        info = wiki.summary(user_command, 5)
        print(info)
        speak(info)
    elif 'open' in user_command:
        user_command = user_command.replace('open ', '')
        speak('opening' + user_command)
        pk.open_web()
    elif 'who are you' in user_command:
        speak_ex('I am your ' + va_name + ', Tell me boss.')
    elif 'are you single' in user_command:
        speak_ex('I dont have any human relations cause I am a chatbot.')       
    elif 'What is Blockchain' in user_command:
        speak_ex('Blockchain is a decentralized and distributed ledger technology that enables secure and transparent record-keeping of transactions across a network of computers. It is the underlying technology behind cryptocurrencies like Bitcoin, but its applications extend beyond digital currencies')                                                                                                                                                                                                                            
        print('Blockchain is a decentralized and distributed ledger technology that enables secure and transparent record-keeping of transactions across a network of computers. It is the underlying technology behind cryptocurrencies like Bitcoin, but its applications extend beyond digital currencies')
    else:
        speak_ex('please say it again boss.') 