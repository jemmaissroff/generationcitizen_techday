import sys, os
import webapp2

sys.path.append('handlers')
sys.path.append('lib')

from View import View
from TextSender import TextSender

application = webapp2.WSGIApplication([ ('/', View),
										('/send', TextSender),
										],
										debug = True)
