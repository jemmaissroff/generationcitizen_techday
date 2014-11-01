import sys, os
import webapp2

sys.path.append('handlers')
sys.path.append('lib')

from View import View
from TextSender import TextSender
from TextResponder import TextResponder

application = webapp2.WSGIApplication([ ('/', View),
										('/send', TextSender),
										('/text', TextResponder)],
										debug = True)
