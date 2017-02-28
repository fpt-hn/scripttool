from twilio.rest import TwilioRestClient


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = "+14012565093"

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+84963012472"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "https://demo.twilio.com/welcome/voice/"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient("ACd3d4e9d3f8d0482f6bca14f006xxxx", "8e967a58c2b1f460ef316e7fcc15xxxx")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)