import webapp2
import urllib2
import json

DEWICK_URL = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=11&locationName=Dewick+MacPhie+Dining+Center&naFlag=1"
CARM_URL = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=09&locationName=Carmichael+Dining+Center&naFlag=1"

class API(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.headers["Content-Type"] = "text/json"
        dewick_page = urllib2.urlopen(DEWICK_URL).read()
        carm_page = urllib2.urlopen(CARM_URL).read()
        d = {}
        d['food'] = 'food'
        d['carm'] = carm_menu
        d['dewick'] = dewick_menu
        str_rep = json.dumps(d, separators=(',',':'))
        self.response.write(str_rep)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>API access @ /API</h1> <a href = "https://github.com/charles-meyer/">click if questions</a>')

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/api', API),
    (r'/api/', API),
], debug=True)

