import getpass
from dataclasses import dataclass
from colorama import Fore,Back
import questionary

aws_access_key_id:str = getpass.getpass('AWS_ACCESS_KEY_ID: ')
aws_secret_access_key:str = getpass.getpass('AWS_SECRET_ACCESS_KEY: ')

'''
MAIN MENU - 1
'''
def dashboard_init():
    print('Welcome to the Dashboard...\n')
    main_menu_selection = questionary.select(
        'Choose from the below services',
        choices=['S3','Kinesis-Datastreams','Kinesis-Firehosestreams']
    ).ask()
    match main_menu_selection:
        case 'S3':
            s3_menu()
 
'''
S3 MENU - 2
'''
def s3_menu()->None:
    print('S3 OPTIONS')


def main()->None:
    dashboard_init()
   
    

if __name__ == "__main__":
    main()