from __future__ import print_function
import os
import os.path
from base64 import urlsafe_b64decode
from bs4 import BeautifulSoup

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
NUMBER_MESSAGES = 5


class Mail:
    def __init__(self):
        self.creds = self.auth()
        self.gmail_service = build('gmail', 'v1', credentials=self.creds)

    def read_message(self, message_id) -> str:
        mail_texts = []
        msg = self.gmail_service.users().messages().get(userId='me', id=message_id, format='full').execute()
        # parts can be the message body, or attachments
        payload = msg['payload']
        parts = payload.get("parts")
        if parts:
            for part in parts:
                mimeType = part.get("mimeType")
                body = part.get("body")
                data = body.get("data", '')
                if data:
                    if mimeType == "text/plain":
                        continue
                        # text = urlsafe_b64decode(data).decode()
                    elif mimeType == "text/html":
                        text = BeautifulSoup(urlsafe_b64decode(data), 'lxml').get_text(strip=True)
                    else:
                        continue
                    mail_texts.append(text)
        return " ".join(mail_texts)

    @staticmethod
    def auth():
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_console(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return creds

    def list_messages(self):
        results = self.gmail_service.users().messages().list(userId='me').execute()
        return results.get('messages', [])

    def list_text_messages(self, message_id=None):
        mail_texts = []
        messages = self.list_messages()
        if not message_id:
            for message in messages[0:NUMBER_MESSAGES]:
                mail_texts.append(self.read_message(message['id']))
        else:
            mail_texts = self.read_message(message_id)
        return mail_texts

