from utils.sentiment_analysis import analyze_sentiment
from utils.email_filters import filter_emails
from services.voice_utils import speak

def check_mails(service):
    results = service.users().messages().list(userId='me', labelIds=["INBOX", "UNREAD"]).execute()
    messages = results.get('messages', [])

    if not messages:
        speak("No new emails.")
    else:
        speak(f"You have {len(messages)} new emails.")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
            sender = next(header['value'] for header in msg['payload']['headers'] if header['name'] == "From")
            snippet = msg['snippet']

            sentiment = analyze_sentiment(snippet)
            speak(f"Email from {sender}. The content sentiment is {sentiment}.")
            speak("Do you want to read it?")
            command = input("Type 'read' to read the email or 'skip' to skip: ").lower()

            if command == 'read':
                speak(snippet)

def send_email(service):
    speak("Who do you want to send an email to?")
    recipient = input("Enter the recipient email: ")
    speak("What is the subject?")
    subject = input("Enter the subject: ")
    speak("What should the email say?")
    body = input("Enter the email body: ")

    message = {
        'raw': base64.urlsafe_b64encode(f"To: {recipient}\nSubject: {subject}\n\n{body}".encode('utf-8')).decode('utf-8')
    }
    service.users().messages().send(userId="me", body=message).execute()
    speak("Email sent successfully.")
