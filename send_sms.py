from twilio.rest import TwilioRestClient
from account import account_sid
from account import auth_token
from account import from_number
# Your Account Sid and Auth Token from twilio.com/user/account
def send_text(body, recipient):
	client = TwilioRestClient(account_sid, auth_token)
	message = client.sms.messages.create(body = body,
	    to = recipient,    
	    from_ = from_number) 
