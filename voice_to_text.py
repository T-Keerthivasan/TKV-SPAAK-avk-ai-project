#Sample prog which doesnt show what stage the program is
'''import speech_recognition as sr

def main():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak something...")
        # Adjust for ambient noise and record the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
'''

##Notes
#Audio Drivers: Make sure your audio drivers are updated to support multiple audio sources.
#Permissions: Sometimes, applications may require permission to access your microphone and audio devices.
#Main Program.
import speech_recognition as sr

def main():
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    
    # Indicate the program is starting
    print("Program started. Waiting for audio input...")

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        
        print("Listening for audio input... Please speak.")
        # Record the audio
        audio = recognizer.listen(source)

        print("Audio input received. Processing...")
        
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        
        print("Program has finished executing.")

while True:
    n=input("Welcome to our project would you like to Enter(Y/N): ")
    if n in 'Yy':
        if __name__ == "__main__":
            main()
    else:
        print("why you quite")
        break
