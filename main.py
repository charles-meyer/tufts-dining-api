import webapp2
import urllib2

class API(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/json"
        self.response.write('{food:food}')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('they have food')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ('/api', API)
], debug=True)

