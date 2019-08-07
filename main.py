import webapp2
import jinja2
import os
from model import Sports
from google.appengine.api import users


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())

    def post(self):
        sports = Sports(
            line1=self.request.get('user-first-ln'), 
            line2=self.request.get('user-second-ln'), 
            sports_type=self.request.get('sports-type')
        )
        sports_key = sports.put()
        self.response.write("Sports created: " + str(sports_key) + "<br>")
        self.response.write("<a href='/Finder'>Sports</a>")

class AllSportsHandler(webapp2.RequestHandler):
    def get(self):
        
        all_sports = Sports.query().fetch()
        
        the_variable_dict = {
            "all_sports": all_sports
        }
        
        Finder_template = the_jinja_env.get_template('templates/finder.html')
        self.response.write(Finder_template.render(the_variable_dict))
        
app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/Finder', AllSportsHandler),
], debug=True)