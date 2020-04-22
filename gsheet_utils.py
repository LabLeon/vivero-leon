import json
import googleapiclient.discovery
from google.oauth2 import service_account
import os


GOOGLE_SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID")

class GSheet:
    google_credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
    gkeys = json.loads(google_credentials_json)

    def __init__(self):
        self.service = self.__get_service()

    def __get_credentials(self):
        scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
        GOOGLE_PRIVATE_KEY = self.gkeys["private_key"]
        # The environment variable has escaped newlines, so remove the extra backslash
        GOOGLE_PRIVATE_KEY = GOOGLE_PRIVATE_KEY.replace('\\n', '\n')

        account_info = {
        "private_key": GOOGLE_PRIVATE_KEY,
        "client_email": self.gkeys["client_email"],
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        }

        credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
        return credentials

    def __get_service(self):
        service_name='sheets'
        api_version='v4'
        credentials = self.__get_credentials()
        service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
        return service

    def get_data(self, range_name):
        result = self.service.spreadsheets().values().get(
                spreadsheetId=GOOGLE_SPREADSHEET_ID, range=range_name
            ).execute()
        values = result.get('values', [])
        return values
