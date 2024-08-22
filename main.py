import webbrowser
import pyttsx3
import speech_recognition as sr
import musicLibrary
import requests


recognizer = sr.Recognizer()
newsapi = "8bf1c251f6ac41efaf1cbfbfc235617b"

def speak(text):
    """This function takes a string as input and converts it into speech."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  # Split the string on the space character and store the second word in the variable and execute the code for that song"
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=8bf1c251f6ac41efaf1cbfbfc235617b")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
                
        
    else:
        # let openAI handle the rest commands
        pass

if __name__ == "__main__":  # This line is missing a space between the two underscores, which is causing the error. The correct syntax is: if __name__ == "__main__"
    speak("Initializing sofia....")
    while True:
    
        r = sr.Recognizer()
        
    # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1.5)
               
        # recognize speech using Google Speech Recognition  
            word = r.recognize_google(audio)
            print(f"recognized word: {word}")
            
            if(word.lower() == "sofia"):
                speak("Yes, what can I do for you?")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
    
        
        except Exception as e:
            print("error; {0}".format(e))
            
            
