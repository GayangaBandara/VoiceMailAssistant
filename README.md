# Voice Email Assistant

Voice Email Assistant is a Python-based project that allows users to send and receive emails using voice commands. This application utilizes speech recognition, natural language processing, and the Gmail API to provide a hands-free email experience.

## Features
- **Send Emails:** Compose and send emails using voice commands.
- **Read Emails:** Listen to received emails using text-to-speech.
- **Sentiment Analysis:** Analyze the sentiment of email content.

## Prerequisites
- Python 3.8 or later
- A Google account with Gmail API enabled
- Required Python libraries (see `requirements.txt`)

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/voice-email-assistant.git
    cd voice-email-assistant
    ```

2. **Set Up a Virtual Environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate    # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Gmail API:**
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a project and enable the Gmail API.
    - Configure OAuth 2.0 credentials.
    - Download the credentials JSON file and save it as `credentials.json` in the project directory.

5. **Install Microphone Support:**
    For Windows:
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```

## Usage

1. **Run the Application:**
    ```bash
    python main.py
    ```

2. **Authenticate Gmail:**
    - A URL will be generated in the console.
    - Open the URL in your browser, log in to your Google account, and grant the required permissions.
    - Copy the authorization code and paste it into the console.

3. **Interact Using Voice Commands:**
    - Say commands like "Send an email" or "Check my emails."

## Project Structure
```
voice-email-assistant/
├── main.py                 # Entry point of the application
├── services/
│   ├── email_manager.py   # Email management functions
│   ├── voice_utils.py     # Voice recognition and text-to-speech utilities
├── utils/
│   ├── sentiment_analysis.py  # Sentiment analysis functions
├── requirements.txt       # Python dependencies
├── credentials.json       # Gmail API credentials
└── README.md              # Project documentation
```

## Acknowledgments
- [TextBlob](https://textblob.readthedocs.io/): For sentiment analysis
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): For voice recognition
- [Gmail API](https://developers.google.com/gmail/api): For email handling