from services.authentication import authenticate_gmail
from services.email_manager import check_mails, send_email
from services.voice_utils import speak, get_audio

def main():
    speak("Initializing voice email assistant.")
    service = authenticate_gmail()

    while True:
        speak("What would you like to do? Check emails or send an email?")
        command = get_audio()

        if "check" in command:
            check_mails(service)
        elif "send" in command:
            send_email(service)
        elif "exit" in command:
            speak("Exiting the assistant. Have a nice day!")
            break
        else:
            speak("I didn't understand. Please try again.")

if __name__ == "__main__":
    main()
