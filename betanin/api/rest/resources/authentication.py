# 3rd party
from flask_jwt_extended import create_access_token

# betanin
from betanin import main_config
from betanin.api.rest.base import BaseResource
from betanin.api.rest.models import request as req_models
from betanin.api.rest.namespaces import authentication_ns


@authentication_ns.route('/login')
class LoginResource(BaseResource):
    @staticmethod
    @authentication_ns.doc(security=None)
    @authentication_ns.doc(parser=req_models.credentials)
    def post():
        'generates a jwt for the given username / password'
        args = req_models.credentials.parse_args()
        config = main_config.read()
        if args['username'] != config['frontend']['username'] \
                or args['password'] != config['frontend']['password']:
            return {"message": "invalid username or password"}, 400
        return {"token": create_access_token(args['username'])}
