import webapp2
import os
import jinja2
from database import *
from google.appengine.api import mail, memcache, channel
import datetime
import urllib
import json
import logging

#Lines for using HTML templates
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates')
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        """Writes to the page."""
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        """Returns as a string the html of the page."""
        t = JINJA_ENV.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        """Renders the page."""
        self.write(self.render_str(template, **kw))
