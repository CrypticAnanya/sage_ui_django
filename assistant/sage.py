def get_reply(user_input):
    return f"Sage response to: {user_input}"
import speech_recognition as sr

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command
    except Exception as e:
        print("Sorry, could not recognize.")
        return ""
