from google.appengine.ext import db
from Handler import Handler 
from database import Text

class View(Handler):
	def render_front(self, sent=0, yes=0, no=0): 
		self.render("metrics.html", sent=sent, yes=yes, no=no)

	def get(self):
		sent = len(list(Text.gql("SELECT * from Text")))
		yes = len(list(Text.gql("SELECT * from Text WHERE Response=Y")))
		no = len(list(Text.gql("SELECT * from Text WHERE Response=N")))
		no_responses = sent - yes - no
		self.render_front(sent, yes, no)
