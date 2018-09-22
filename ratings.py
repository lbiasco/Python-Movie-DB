import cherrypy
import re, json

class RatingsController(object):
    
    def __init__(self, ooapi):
        self.db = ooapi

    def GET_MID(self, mid):
        output = {'result':'success'}
        movie = self.db.get_movie(mid)
        if(movie == None):
            output['result'] = 'error'
            output['message'] = 'No movie exists at ' + str(mid)
            return json.dumps(output)
        try:
            output['rating'] = self.db.get_rating(mid)
            output['movie_id'] = int(mid)
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)
