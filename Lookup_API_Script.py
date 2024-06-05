# Lookup v2 API | Twilio
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Create an instance of the Client class (to initialize API)
client = Client(account_sid, auth_token)

while True:
    number = '+' + '1' + input("Please enter a ten digit U.S. telephone number: ")

    # Call methods to fetch lookup information
    phone_number = client.lookups \
                         .v2 \
                         .phone_numbers(number) \
                         .fetch(fields='line_type_intelligence,caller_name')

    if phone_number.valid:
        print()
        print(f'{phone_number.national_format} is a valid number.')
        print()
    else:
        print()
        print(f'{phone_number.phone_number} is not a valid number.')

    print("Here are some more details about this phone number:")

    print(phone_number.caller_name, phone_number.line_type_intelligence)
    print()

    continuing = input('Would you like to search another number? ').lower()
    print()

    if continuing in ['y', 'yes']:
        continue
    else:
        break

quit()
