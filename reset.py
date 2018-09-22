import cherrypy
import re, json

class ResetController(object):
    
    def __init__(self, ooapi):
        self.db = ooapi

    def PUT_INDEX(self):
        output = {'result':'success'}
        self.db.load_all_preset()
        return json.dumps(output)

    def PUT_MID(self, mid):
        output = {'result':'success'}
        self.db.load_movie_preset(mid)
        return json.dumps(output)
