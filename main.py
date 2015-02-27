import webapp2
import urllib2

DINING_HALL_URLS = ["http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=11&locationName=Dewick+MacPhie+Dining+Center&naFlag=1",
                    "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=09&locationName=Carmichael+Dining+Center&naFlag=1"]


class API(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/json"
        self.response.write('{food:food}')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>API access @ /API</h1> <a href = "https://github.com/charles-meyer/">click if questions</a>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ('/api', API)
], debug=True)

