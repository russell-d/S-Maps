from google.appengine.ext import ndb

class Sports3(ndb.Model):
    name = ndb.StringProperty(required=True)
    park = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)
    sports_type = ndb.StringProperty(required=False)    