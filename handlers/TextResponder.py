from twilio.rest import TwilioRestClient
from google.appengine.ext import db
from Handler import Handler
from database import Text
from account import *

class TextResponder(Handler):
	def get(self):
		body = self.request.get('Body')
		sender = self.request.get('From')[2:]
		txt = db.GqlQuery("SELECT * FROM Text WHERE phone_number='" + sender + "'").get()
		if(body.lower() == 'yes'):
			txt.response = 'Y'
		elif(body.lower() == 'no'):
			txt.response = 'N'
		txt.put()

