import cherrypy
import re, json

class RecommendationsController(object):
    
    def __init__(self, ooapi):
        self.db = ooapi

    def GET_UID(self, uid):
        output = {'result':'success'}
        rec = self.db.get_recommendation(uid)
        if(rec == None):
            output['message'] = 'No recommendation'
            return json.dumps(output)
        try:
            output['movie_id'] = rec
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)

    def PUT_UID(self, uid):
        output = {'result':'success'}
        req = json.loads(cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length'])))
        self.db.set_user_movie_rating(uid, req['movie_id'], req['rating'])
        return json.dumps(output)

    def DELETE_INDEX(self):
        output = {'result':'success'}
        self.db.delete_all_ratings()
        return json.dumps(output)
