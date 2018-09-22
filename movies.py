import cherrypy
import re, json

class MoviesController(object):
    
    def __init__(self, ooapi):
        self.db = ooapi

    def GET_INDEX(self):
        output = {'result':'success'}
        try:
            output['movies'] = self.db.get_movies()['movies']
        except (KeyError, TypeError) as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)

    def GET_MID(self, mid):
        output = {'result':'success'}
        movie = self.db.get_movie(mid)
        try:
            output['title'] = movie['title']
            output['genres'] = movie['genres']
            output['id'] = int(movie['id'])
            output['img'] = movie['img']
        except (KeyError, TypeError) as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)

    def POST_INDEX(self):
        output = {'result':'success'}
        mid = max(self.db.get_movies()['movies'], key=int)+1
        req = json.loads(cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length'])))
        req['id'] = int(mid)
        req['img'] = '/default.jpg'
        self.db.set_movie(mid, req)        
        try:
            output['id'] = int(mid)
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)

    def PUT_MID(self, mid):
        output = {'result':'success'}
        req = json.loads(cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length'])))
        req['id'] = int(mid)
        req['img'] = '/default.jpg'
        self.db.set_movie(mid, req)
        return json.dumps(output)

    def DELETE_INDEX(self):
        output = {'result':'success'}
        self.db.delete_movies()
        return json.dumps(output)

    def DELETE_MID(self, mid):
        output = {'result':'success'}
        self.db.delete_movie(mid)
        return json.dumps(output)
