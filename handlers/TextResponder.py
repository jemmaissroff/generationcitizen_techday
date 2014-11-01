from twilio.rest import TwilioRestClient
from google.appengine.ext import db
from Handler import Handler
from database import Text
from account import *

class TextSender(Handler):
	def render_front(self):
		self.render("textresponder.html")

	def get(self):
		body = self.request.get('Body')
		sender = self.request.get('From')
		txt = db.GqlQuery("SELECT * FROM Text Where sender = :1", sender)
		if(body.lower() == "yes"):
			txt.response = yes
		elif(body.lower() == "no"):
			txt.response

	def post(self):
		pass
