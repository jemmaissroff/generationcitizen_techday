from twilio.rest import TwilioRestClient
from google.appengine.ext import db
from Handler import Handler
from database import Text
from account import *

class TextSender(Handler):
	def render_front(self):
		self.render("textsender.html")

	def get(self):
		self.render_front()

	def post(self):
		client = TwilioRestClient(account_sid, auth_token)
		body = "Do you support {OUR IDEA}? Respond yes or no."
		recipient = self.request.get("number")
		message = client.sms.messages.create(body=body, to=recipient, from_=from_number)
		txt = Text(phone_number=recipient, response=None, sent_message = body)
		txt.put()
		self.redirect("/")
