import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import random
import webbrowser
import os
import smtplib
from youtube_search import YoutubeSearch
from googlesearch import search

speech_engine=pyttsx3.init("sapi5")
voices=speech_engine.getProperty("voices")
rate=speech_engine.getProperty("rate")

# print(voices[0].id)

# or
# for voice in voices:
#     print(voice.id)
speech_engine.setProperty("voice",voices[0].id)
speech_engine.setProperty("rate",rate-80)

def speak(audio):
    speech_engine.say(audio)
    speech_engine.runAndWait()


def wishme():
    current_hour=(datetime.datetime.now().hour)
    if (current_hour>4 and current_hour<12):
        speak("Good Morning Mayank")

    elif (current_hour>=12 and current_hour<17):
        speak("Good Afternoon Mayank")

    elif (current_hour>=17 and current_hour<=19):
        speak("Good Evening Mayank")

    else:
        speak("Good Night Mayank")
        
    speak("Hey I'am Freddy.\n Sir, please tell me how may i help you")

def take_command():
    command_recognize=sr.Recognizer()
    with sr.Microphone() as source_microphone:
        print("Listening....")
        speak("Listening")
        command_recognize.pause_threshold=1
        commands=command_recognize.listen(source_microphone)

    try:
        print("Recognizing....") 
        speak("Recognizing")
        enquiry=command_recognize.recognize_google(commands,language="en-in")
        print(f"User said :- {enquiry}\n")
        return enquiry
    except:
        audio="Please say that again"
        print(audio)
        speak(audio)
        return "None"
    

def send_mail(to,content):
    new_file=open(r"E:\mayankvscode\projects\ps.txt")
    # 1- unsecured connection
    server=smtplib.SMTP("smtp.gmail.com",587)
    # 2- secured connection
    # server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.ehlo()
    server.starttls() # secured connection
    server.login("macrobell.service@gmail.com",new_file.read())
    new_file.close()
    server.sendmail("macrobell.service@gmail.com",to,content)
    server.close()

receivers_dict={
    "mayank":"mayankmystery18@gmail.com",
    "rocco":"18excaliber1997@gmail.com",
    "amazon":"support@amazon.com",
    "hdfc bank":"support@hdfcbank.com",
    "myntra":"support@myntra.com"
}

if (__name__=="__main__"):
    wishme()
    while True:
        enquiry=take_command().lower()
        # 1- searching on wikipedia 

        if ("wikipedia" in enquiry):
            print("Searching Wikipedia")
            enquiry=enquiry.replace("wikipedia","")
            try:
                search_result=wikipedia.summary(enquiry,sentences=2)
            except wikipedia.exceptions.DisambiguationError as err:
                random_item=random.choice(err.options)
                search_result=wikipedia.summary(random_item,sentences=2)
            speak("According to wikipedia")
            print(search_result)
            speak(search_result)

        # 2- searching for any website on browser
        elif ("open google" in enquiry):
            speak("what you wanna search on google")
            searching_key=take_command().lower()
            if (searching_key!= "none"):
                results=search(searching_key,tld=".com",stop=15,pause=2.0)
                c,d=1,{}
                print("Here are the links :-\n")
                for i in results:
                    print(f"{c} : {i}")
                    d[c]=i
                    c+=1
                speak("which link you wanna open")
                link_number=take_command()
                if (int(link_number) in d):
                    resulting_link=d.get(int(link_number))
                    webbrowser.open(resulting_link)


        elif ("open youtube" in enquiry):
            speak("what you wanna search on youtube")
            searching_key=take_command().lower()
            if (searching_key!= "none"):
                results=YoutubeSearch(searching_key,max_results=10).to_dict()
                if (searching_key=="songs" or searching_key=="song"):
                    c=1
                    d={}
                    print("songs :-\n")
                    for i in results:
                        print(c,":",i["title"]) # print(f"{c} : {i["title"]}") will not work
                        d[c]=i
                        c+=1
                    speak("which song you wanna play")
                    song_number=take_command()
                    if (int(song_number) in d):    
                        resulting_link="youtube.com"+(d.get(int(song_number))).get("link")
                        webbrowser.open(resulting_link)

                c,d=1,{}
                print(f"{searching_key} :-\n")
                for i in results:
                    print(c,":",i["title"])
                    d[c]=i
                    c+=1
                speak("which video do you wanna play")
                video_number=take_command()
                if (int(video_number) in d):
                    resulting_link="youtube.com"+(d.get(int(video_number))).get("link")
                    webbrowser.open(resulting_link)  


        elif ("open github" in enquiry):
            enquiry=enquiry.replace("open","")
            print(f"Opening {enquiry}")
            webbrowser.open("github.com")

        elif ("open stackoverflow" in enquiry):
            enquiry=enquiry.replace("open","")
            print(f"Opening {enquiry}")
            webbrowser.open("stackoverflow.com")

        elif ("open geekforgeeks" in enquiry):
            enquiry=enquiry.replace("open","")
            print(f"Opening {enquiry}")
            webbrowser.open("geekforgeeks.org")

        elif ("open gmail" in enquiry):
            enquiry=enquiry.replace("open","")
            print(f"Opening {enquiry}")
            webbrowser.open("gmail.com")

        elif ("open twitter" in enquiry):
            enquiry=enquiry.replace("open","")
            print(f"Opening {enquiry}")
            webbrowser.open("twitter.com")

        elif ("open linkedin" in enquiry):
            enquiry=enquiry.replace("open","")
            print(f"Opening {enquiry}")
            webbrowser.open("linkedin.com")

        # 3- checking the current time
        elif ("current time" in enquiry):
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            speak(current_time)

        # 4- stopping the Freddy
        elif ("bye-bye" in enquiry):
            speak("bye-bye Mayank")
            break

        # 5- checking today's date
        elif ("today's date" in enquiry):
            date_mon_year=datetime.datetime.now().strftime("%d-%m-%y")
            print(date_mon_year)
            speak(date_mon_year)
        
        # 6- opening git-bash
        elif ("open git bash" in enquiry):
            git_bash_path=r"C:\Program Files\Git\git-bash.exe"
            speak("opening git bash")
            os.startfile(git_bash_path)

        # 7- playing music
        elif ("play music" in enquiry):
            music_path=r"E:\mayank\music"
            music_files=os.listdir(music_path)
            music_files_path=os.path.join(music_path,random.choice(music_files))
            os.startfile(music_files_path)

        # 8- writing inside a text document 
        elif ("write a text" in enquiry):
            textfile_path=r"E:\mayankvscode\projects\texts"
            speak("what should be the file name")
            file_name=take_command().lower()
            file_name=file_name+".txt"
            file_name_path=os.path.join(textfile_path,file_name)
            with open(file_name_path,"w") as new_file:
                speak("what should i write")
                write_text=take_command().lower()
                new_file.write(write_text)
                speak("written successfully")
                os.startfile(file_name_path)


        # 9- sending e-mails 
        elif ("send mail" in enquiry):
            speak("to whome i will send the mail")
            receiver=take_command().lower()
            to=receivers_dict.get(receiver)
            speak("what should i speak")
            content=take_command()
            try:
                send_mail(to,content)
                speak("mail sent successfully")
            except:
                speak("failed to sent mail")

        # 10- reading files 

        elif ("open file" in enquiry):
            file_path=r"E:\mayankvscode\exercise"
            files=os.listdir(file_path)
            speak("file name please")
            file_name=take_command().lower()
            file_name=file_name+".py"
            if (file_name in files):
                file_new_path=os.path.join(file_path,file_name)
                with open(file_new_path) as new_file:
                    speak("can i read the file")
                    response=take_command().lower()
                    if (response=="yes"):
                        read_file=new_file.read()
                        speak(read_file)
                    elif (response=="no"):
                        os.startfile(file_new_path)





            
            


