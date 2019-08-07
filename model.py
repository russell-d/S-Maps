from google.appengine.ext import ndb

class Sports(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.IntegerProperty(required=True)
    sports_type = ndb.StringProperty(required=False)