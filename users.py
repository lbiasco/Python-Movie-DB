import cherrypy
import re, json

class UsersController(object):
    
    def __init__(self, ooapi):
        self.db = ooapi

    def GET_INDEX(self):
        output = {'result':'success'}
        try:
            output['users'] = self.db.get_users()['users']
        except (KeyError, TypeError) as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)

    def GET_UID(self, uid):
        output = {'result':'success'}
        user = self.db.get_user(uid)
        try:
            output['gender'] = user['gender']
            output['age'] = user['age']
            output['occupation'] = user['occupation']
            output['zipcode'] = user['zipcode']
            output['id'] = int(user['id'])
        except (KeyError, TypeError) as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)

    def POST_INDEX(self):
        output = {'result':'success'}
        uid = int(max(self.db.get_users()['users'], key=int))+1
        req = json.loads(cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length'])))
        req['id'] = int(uid)
        self.db.set_user(int(uid), req)        
        try:
            output['id'] = int(uid)
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)

    def PUT_UID(self, uid):
        output = {'result':'success'}
        req = json.loads(cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length'])))
        req['id'] = int(uid)
        self.db.set_user(uid, req)
        return json.dumps(output)

    def DELETE_INDEX(self):
        output = {'result':'success'}
        self.db.delete_users()
        return json.dumps(output)

    def DELETE_UID(self, uid):
        output = {'result':'success'}
        self.db.delete_user(uid)
        return json.dumps(output)
