from google.appengine.ext import db

#Table for Users
class Text(db.Model):
	phone_number = db.StringProperty(required=True)
	response = db.StringProperty(required=False) # Y for yes, N for no, None for no response
	sent_message = db.TextProperty(required=True)
	received_message = db.TextProperty(required=False)
