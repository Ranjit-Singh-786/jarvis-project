import pyttsx3
# import speech_recognition
engine = pyttsx3.init('sapi5')            #initlize sapi5 system
sound = engine.getProperty('voices')      #fatched voice in sapi5 window
# print(sound[0].id)    #[0] for boy voice and this is print for chek the voice 
engine.setProperty('sound',sound[0].id)    #set for voice david
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   

if __name__== "__main__":
    speak("jai maataa dee ")










# import datetime
# corrent_time_and_date=datetime.datetime.now()
# hour = datetime.datetime.now().hour
# minute = datetime.datetime.now().minute
# second = datetime.datetime.now().second
# print(corrent_time_and_date)
# hour = int(input("enter your hour:- "))
# if hour > 0 and hour < 12 :
#     print("good morning")
# elif hour >= 12 and hour <=18:
#     print("good afternoon")
# else:
#     print("good evening")


# if __name__ == "__main__" :          #this is nothing this is true condition
#     print('jai mata di')
# else:
#     print("not equal")