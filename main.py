import webapp2
import urllib2
import json

class API(webapp2.RequestHandler):
    def get(self, dining_hall=None):
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.headers["Content-Type"] = "text/json"
        d = {}
        d['food'] = 'food'
        if dining_hall:
            d['dining_hall'] = dining_hall
        str_rep = json.dumps(d, separators=(',',':'))
        self.response.write(str_rep)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.write('they have food')

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/api', API),
    (r'/api/(dewick|carm)', API)
], debug=True)

