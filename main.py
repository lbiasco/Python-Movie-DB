import cherrypy
from _movie_database import _movie_database
from movies import MoviesController
from users import UsersController
from recommendations import RecommendationsController
from ratings import RatingsController
from reset import ResetController

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    
    conf = {    'global'    :   {'server.socket_host' : 'student04.cse.nd.edu' , 
                                 'server.socket_port' : 52011},
                '/'         :   {'request.dispatch' : dispatcher}  }

    mdb = _movie_database()
    mdb.load_all_preset()

    moviesCon = MoviesController(mdb)
    dispatcher.connect('movies_index_get', '/movies/', controller=moviesCon, action='GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('movies_mid_get', '/movies/:mid', controller=moviesCon, action='GET_MID', conditions=dict(method=['GET']))
    dispatcher.connect('movies_index_post', '/movies/', controller=moviesCon, action='POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('movies_mid_put', '/movies/:mid', controller=moviesCon, action='PUT_MID', conditions=dict(method=['PUT']))
    dispatcher.connect('movies_index_delete', '/movies/', controller=moviesCon, action='DELETE_INDEX', conditions=dict(method=['DELETE']))
    dispatcher.connect('movies_mid_delete', '/movies/:mid', controller=moviesCon, action='DELETE_MID', conditions=dict(method=['DELETE']))

    usersCon = UsersController(mdb)
    dispatcher.connect('users_index_get', '/users/', controller=usersCon, action='GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('users_uid_get', '/users/:uid', controller=usersCon, action='GET_UID', conditions=dict(method=['GET']))
    dispatcher.connect('users_index_post', '/users/', controller=usersCon, action='POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('users_uid_put', '/users/:uid', controller=usersCon, action='PUT_UID', conditions=dict(method=['PUT']))
    dispatcher.connect('users_index_delete', '/users/', controller=usersCon, action='DELETE_INDEX', conditions=dict(method=['DELETE']))
    dispatcher.connect('users_uid_delete', '/users/:uid', controller=usersCon, action='DELETE_UID', conditions=dict(method=['DELETE']))

    recCon = RecommendationsController(mdb)
    dispatcher.connect('recommendations_uid_get', '/recommendations/:uid', controller=recCon, action='GET_UID', conditions=dict(method=['GET']))
    dispatcher.connect('recommendations_uid_put', '/recommendations/:uid', controller=recCon, action='PUT_UID', conditions=dict(method=['PUT']))
    dispatcher.connect('recommendations_index_delete', '/recommendations/', controller=recCon, action='DELETE_INDEX', conditions=dict(method=['DELETE']))

    ratingsCon = RatingsController(mdb)
    dispatcher.connect('ratings_mid_get', '/ratings/:mid', controller=ratingsCon, action='GET_MID', conditions=dict(method=['GET']))

    resetCon = ResetController(mdb)
    dispatcher.connect('reset_index_put', '/reset/', controller=resetCon, action='PUT_INDEX', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_mid_put', '/reset/:mid', controller=resetCon, action='PUT_MID', conditions=dict(method=['PUT']))

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
    start_service()

