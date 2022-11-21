from __future__ import print_function

import os.path
import requests

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def people_api_paginate_10():
    """
    Return the name(s) of the first 10 connections.
    """
    creds = None
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'src/database/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

    try:
        service = build('people', 'v1', credentials=creds)
        name_array = []

        # Call the People API

        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=10,
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:
            names = person.get('names', [])
            if names:
                name = names[0].get('displayName')
                name_array.append(name)
        
        return name_array
                    
    except HttpError as err:
        print(err)

def people_api_all_person_connection():
    """
    Get all the names in a person connection
    """
    creds = None
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'src/database/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

    try:
        service = build('people', 'v1', credentials=creds)
        people_information = []

        results = service.people().connections().list(
            resourceName='people/me',
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:

            people_person_contacts = {
                "name": "",
                "email": ""
            }

            names = person.get('names', [])
            emails = person.get("emailAddresses", [])

            if names:
                name = names[0].get('displayName')
                people_person_contacts["name"] = name

            if emails:
                email = emails[0].get("value")
                people_person_contacts["email"] = email

            people_information.append(people_person_contacts)

        return people_information
                    
    except HttpError as err:
        print(err)
