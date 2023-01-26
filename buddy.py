from sys import path
import pyttsx3
import wikipedia
import webbrowser
import os
import datetime
import pywhatkit  # for whatsapp msg
import speech_recognition as sr
import random
import smtplib  # to send mail
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # In pascal Case


def TakeInput():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(Source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('user said : ', query)
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return 'None'
    return query


def sendMail(to, content):
    data = os.environ.get("EMAIL PASSWORD")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.environ.get("EMAIL"), f'{data}')
    server.sendmail(os.environ.get("EMAIL"), f'{to}', f"{content}")
    server.close()
    t.close()


def WishMe():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak('Good Morning')
    elif time >= 12 and time < 16:
        speak('Good Afternoon')
    elif time >= 16 and time < 20:
        speak('Good Evening')
    else:
        speak('Good Night')
    speak("I am your buddy, may i help you")


if (__name__ == '__main__'):
    # speak('hello')
    WishMe()
    while (True):
        query = TakeInput().lower()
        if 'wikipedia' in query:
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(result)
        elif ('open youtube' or 'open youtube for me') in query:
            webbrowser.open('youtube.com')
        elif ('open google' or 'open google homepage for me' or 'open google for me') in query:
            webbrowser.open('google.com')
        elif('open facebook' or 'open facebook for me') in query:
            webbrowser.open('facebook.com')
        elif('open amazon' or 'open amazon for me') in query:
            webbrowser.open('amazon.com.in')
        elif('open flipkart' or 'open flipkart for me') in query:
            webbrowser.open('flipkart.com')
        elif('open chess' or 'open chess for me' or 'i want to play chess') in query:
            webbrowser.open('chess.com')
        elif('open whatsapp' or 'open whatsapp for me') in query:
            webbrowser.open('web.whatsapp.com')
        elif('send message' or 'send message on whatsapp') in query:
            d = {}
            speak("whom you want to send it")
            p = TakeInput()
            if f'{p}' in d.keys():
                num = d[p]
                speak('What is the message')
                msg = str(TakeInput())
                h = int(datetime.datetime.now().strftime("%H"))
                m = int(datetime.datetime.now().strftime('%M'))
                pywhatkit.sendwhatmsg(f'+{int(num)}', f'{msg}', h, m+1)
            else:
                speak('that name is not available in your whats app contacts')
        elif ('open stackoverflow') in query:
            webbrowser.open('stackoverflow.com')
        elif ('play music' or 'play song' or 'play a music for me' or 'play a song for me') in  query:
            music_dir='D:\\Music'
            music=os.listdir(music_dir)
            r=random.randint(0,int(len(music)))
            os.startfile(os.path.join(music_dir,music[0]))
        elif ('the time' or 'the time is' or 'what is the time now') in query:
            h = int(datetime.datetime.now().strftime("%H"))
            m = int(datetime.datetime.now().strftime('%M'))
            if h > 12:
                speak(f'the time is {h-12}hours and {m}minutes PM')
            else:
                speak(f'the time is {h}hours and {m}minutes AM')
        elif 'open gaana' in query:
            webbrowser.open('gaana.com')
        elif ('open code' or ' open vs code') in query:
            path = "C:\\Users\\Rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif ('open chrome' or ' open chrome for me') in query:
            path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(path)
        elif ('open edge' or ' open microsoft edge ') in query:
            path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(path)
        elif 'aapke papa aaye hain' in query:
            speak('namaste pappa what I can do for you')
        elif('send mail' or 'send mail using gmail') in query:
            d = {'Navneet':'navneetsinha2003@gmail.com','harsh': 'yadavharsh545@gmail.com', 'surendra': 'yadav.surendra350@gmail.com', 'mine': 'rahulkumar2661984@gmail.com',
                 'to my another mail account': 'rahul.yaduwanshi007@gmail.com', 'to me': 'itsrahulranjan7@gmail.com',('Bablu'or'bablu'):'bk9708166877@gmail.com',('Ayush'or'ayush'):'ayushpandey2262@gmail.com'}
            speak("whom you want to send it")
            p = TakeInput()
            if f'{p}' in d.keys():
                mail = d[p]
                speak('What is the mail')
                body = TakeInput()
                try:
                    sendMail(mail, body)
                    speak('Your mail is successfully sent')
                except Exception as e:
                    print(e)
                    speak('try again later')            
                    # speak('something went wrong please try again later')
        elif ('open ola movies' or 'movies website') in query:
            webbrowser.open('olamovies.top')
        elif ('quit') in query:
            speak('Thank you for using this virtual assistant  hope you enjoyed')
            exit()
