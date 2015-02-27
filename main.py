import webapp2
import httplib
import urllib2
import json

DEWICK_URL = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=11&locationName=Dewick+MacPhie+Dining+Center&naFlag=1"
DEWICK_URL = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=11&locationName=Dewick+MacPhie+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus&myaction=read&dtdate=3%2F1%2F2015"
CARM_URL = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts+Dining&locationNum=09&locationName=Carmichael+Dining+Center&naFlag=1"

class API(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.headers["Content-Type"] = "text/json"
        while True:
            try:
                dewick_page = urllib2.urlopen(DEWICK_URL).read()
                carm_page = urllib2.urlopen(CARM_URL).read()
                break
            except httplib.HTTPException:
                pass
        d = {}
        d['food'] = 'food'
        d['dewick'] = self.parse(dewick_page)
        d['carm'] = self.parse(carm_page)
        str_rep = json.dumps(d, separators=(',',':'))
        self.response.write(str_rep)

    def parse(self, page):
        d = {}
        meals = page.split('shortmenumeals')[1:] #[useless, bfast, lunch, dinner]
        for meal in meals:
            meal_name = meal.split('</div>')[0].split('>')[1]
            categories = meal.split('shortmenucats')[1:]
            d[meal_name] = {}
            for category in categories:
                cat_name = category.split('-- ')[1].split(' --')[0].title()
                items = category.split('closeDescWin()">')[1:]
                items = [item.split('</a')[0] for item in items]
                d[meal_name][cat_name] = items
        return d


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>API access @ /API</h1> <a href = "https://github.com/charles-meyer/">click if questions</a>')

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/api', API),
    (r'/api/', API),
], debug=True)

