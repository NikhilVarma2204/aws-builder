import getpass
from dataclasses import dataclass
from colorama import Fore,Back
import questionary

aws_access_key_id:str = getpass.getpass('AWS_ACCESS_KEY_ID: ')
aws_secret_access_key:str = getpass.getpass('AWS_SECRET_ACCESS_KEY: ')

'''
MAIN MENU 
'''
def dashboard_init():
    print('Welcome to the Dashboard...\n')
    while True:
        main_menu_selection = questionary.select(
        'Choose from the below services',
        choices=['S3','Kinesis-Datastreams','Kinesis-Firehosestreams','Exit']
        ).ask()

        match main_menu_selection:
            case 'S3':
                s3_menu()
            case 'Kinesis-Datastreams':
                kinesis_datastream_menu()
            case 'Kinesis-Firehosestreams':
                kinesis_datafirehose_menu()
            case 'Exit':
                print(Fore.RED,'Script terminated.')
                exit()
            
 
'''
S3 Menu - 1
'''
def s3_menu()->None:
    print(Fore.YELLOW,'Choose from the below ')

'''
Kineis Data Streams Menu - 2
'''
def kinesis_datastream_menu()->None:
    print(Fore.YELLOW,'Choose from Below Kinesis DataStream Options: ')

'''
Kinesis Data Firehose Streams - 3
'''
def kinesis_datafirehose_menu()->None:
    print(Fore.YELLOW,'Choose form below Firehose Options')


def main()->None:
    dashboard_init()
   
    

if __name__ == "__main__":
    main()