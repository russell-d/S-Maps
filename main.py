import webapp2
import jinja2
import os
from model import Sports3
from google.appengine.api import users
import logging
from random import shuffle


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
    
        
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())
    
    def post(self):
        
        # self.response.write("%s %s %s %s %s" % (Sports2.name, Sports2.park, Sports2.time, Sports2.date, Sports2.sports_type))
        
        sports = Sports3(
            name = self.request.get('user-first-ln'),
            park = self.request.get('user-second-ln'),
            time = self.request.get('user-third-ln'),
            date = self.request.get('user-fourth-ln'),
            sports_type = self.request.get('sports-type')
            )
        
        sports.put()
        self.response.write("Sports created: "  + "<br>")
        self.response.write("<a href='/Finder'>Sports</a>")
       
class AllSportsHandler(webapp2.RequestHandler):
    
    def get(self):
        all_sports = Sports3.query().fetch()
        
        sports_dict = {
            'all_sports' : all_sports
        }
        
        latLong = "{lat: 36.598339, lng : -121.896431}"
        myDict = {
            'key': unicode(latLong,"utf-8"),
            'all_sports' : all_sports
        }
        
        finder_template =the_jinja_env.get_template('templates/finder.html')
        self.response.write(finder_template.render(myDict))

    
app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/Finder', AllSportsHandler),
], debug=True)