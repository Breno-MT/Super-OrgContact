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
    Get all the 10 persons information in a person connection
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

        people_domain_conectanuvem = []
        people_domain_gmail = []

        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=10,
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:

            people_person_contacts = {
                "domain": "",
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
                
                if "@conectanuvem" in email:
                    people_person_contacts["domain"] = "ConectaNuvem"
                    people_person_contacts["name"] = name
                    people_person_contacts["email"] = email
                    people_domain_conectanuvem.append(people_person_contacts)

                if "@gmail" in email:
                    people_person_contacts["domain"] = "Gmail"
                    people_person_contacts["name"] = name
                    people_person_contacts["email"] = email
                    people_domain_gmail.append(people_person_contacts)


            people_information.append(people_person_contacts)

        return people_domain_conectanuvem, people_domain_gmail, people_information
                    
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

        people_domain_conectanuvem = []
        people_domain_gmail = []

        results = service.people().connections().list(
            resourceName='people/me',
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:

            people_person_contacts = {
                "domain": "",
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
                
                if "@conectanuvem" in email:
                    people_person_contacts["domain"] = "ConectaNuvem"
                    people_person_contacts["name"] = name
                    people_person_contacts["email"] = email
                    people_domain_conectanuvem.append(people_person_contacts)

                if "@gmail" in email:
                    people_person_contacts["domain"] = "Gmail"
                    people_person_contacts["name"] = name
                    people_person_contacts["email"] = email
                    people_domain_gmail.append(people_person_contacts)


            people_information.append(people_person_contacts)

        return people_domain_conectanuvem, people_domain_gmail, people_information
                    
    except HttpError as err:
        print(err)
