import webapp2
import urllib2

DEWICK_URL = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=11&locationName=Dewick+MacPhie+Dining+Center&naFlag=1"
CARM_URL = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=09&locationName=Carmichael+Dining+Center&naFlag=1"

class API(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/json"
        self.response.write('{food:food}')
        dewick_page = urllib2.urlopen(DEWICK_URL).open
        carm_page = urllib2.urlopen(CARM_URL).open


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>API access @ /API</h1> <a href = "https://github.com/charles-meyer/">click if questions</a>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ('/api', API)
], debug=True)

