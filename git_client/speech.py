import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
from playsound import playsound

def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
    
def main():

    # welcome_text = "Quarto utente"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save(".\audio\4_user.mp3")
    #playsound("welcome.mp3")
    
    # welcome_text = "Benvenuto! Cosa posso fare? I comandi disponibili sono: Registrazione Login"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("welcome.mp3")
    # playsound("welcome.mp3")

    # welcome_text = "Esci"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/exit.mp3")

    # welcome_text = "A presto"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/see_you.mp3")

    # welcome_text = "Dimmi un comando"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/command.mp3")

    # welcome_text = "Il nome inserito è corretto?"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/control_name.mp3")

    # welcome_text = "Il cognome inserito è corretto?"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/control_surname.mp3")

    # welcome_text = "Il numero inserito è corretto?"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/control_number.mp3")

    # welcome_text = "Dimmi pronto quando sei davanti la videocamera"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/say_right.mp3")


    # welcome_text = "Faccia non riconosciuta,riprovare"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/unknown_face.mp3")

    # welcome_text = "Nessuna risposta rilevata, ripetere"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/unknown_response.mp3")

    # welcome_text = "Utente già presente"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/user_again.mp3")

    # welcome_text = "Registrazione avvenuta con successo"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/successful_registration.mp3")

    # welcome_text = "Registrazione fallita"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/unsuccessful_registration.mp3")

    # welcome_text = "Login avvenuto con successo"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("./audio/successful_login.mp3")

    welcome_text = "Adesso mostreremo la selezione di film che abbiamo fatto per voi; dite il numero corrispondente al film che vi interessa"
    myobj = gTTS(text=welcome_text,lang="it",slow=False)
    myobj.save('./audio/choose_film.mp3')




    
    
    
    # welcome_text = "I comandi disponibili sono:"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("commands_intro.mp3")
    # welcome_text = "Registrazione"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("reg.mp3")
    # welcome_text = "Login"
    # myobj = gTTS(text=welcome_text,lang="it",slow=False)
    # myobj.save("log.mp3")
    # '''
    # '''
    # print("Start recognition \n")
    # r = sr.Recognizer()
    # text = ""
    # with sr.Microphone() as source:
    #     r.adjust_for_ambient_noise(source)
    #     print("Sono in ascolto...parla pure!")
    #     audio = r.listen(source)
    #     print("ok! sto elaborando il messaggio")
    #     try:
    #         text = r.recognize_google(audio,language="it-IT")
    #         print("Ho capito: \n",text)
    #     except Exception as e:
    #         print(e)
    # if(text=="saluta"):
    #     hello_text = "Ciao Fabiana"
    #     myobj = gTTS(text=hello_text,lang="it",slow=False)
    #     myobj.save("hello.mp3")
    #     playsound("hello.mp3")
    
    
if __name__ == "__main__":
	main()