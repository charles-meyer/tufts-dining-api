import webapp2
import urllib2
import json

DINING_HALL_URLS = {"dewick":"http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=11&locationName=Dewick+MacPhie+Dining+Center&naFlag=1",
                    "carm":"http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=09&locationName=Carmichael+Dining+Center&naFlag=1"}


class API(webapp2.RequestHandler):
    def get(self, dining_hall=None):
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.headers["Content-Type"] = "text/json"
        d = {}
        d['food'] = 'food'
        if dining_hall:
            d['dining_hall'] = dining_hall
            d['url'] = DINING_HALL_URLS[dining_hall]
        str_rep = json.dumps(d, separators=(',',':'))
        self.response.write(str_rep)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>API access @ /API</h1> <a href = "https://github.com/charles-meyer/">click if questions</a>')

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/api', API),
    (r'/api/(dewick|carm)', API)
], debug=True)

