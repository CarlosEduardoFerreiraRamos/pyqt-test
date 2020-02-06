import json
from six.moves.urllib.request import urlopen
from functools import wraps

from jose import jwt


from util import get_command_prop

from auth.manager import AuthServer

from configuration.manager import ConfigurationManager, ConfigProp

# realm = KeycloakRealm(server_url='http://localhost:8080', realm_name='dev')

# client = realm.open_id_connect('omt-server','a9433638-d008-409e-9a27-6b6c20a5e02e' )




server = AuthServer()

client = server.create_connection_client(ConfigurationManager.get_config_value(ConfigProp.auth_client_id()),ConfigurationManager.get_config_value(ConfigProp.auth_client_secret()))

def build_auth_function():
    is_prod = get_command_prop('--PROD') is not None

    def prod_auth(token):
        """
        Referense https://auth0.com/docs/quickstart/backend/python
        """
        try:
            AUTH0_DOMAIN = 'dev-31b5r0mn.auth0.com'
            API_AUDIENCE = 'https://omt-auth'
            ALGORITHMS = ["RS256"]
            jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
            print('jsonurl',jsonurl)
            jwks = json.loads(jsonurl.read())
            print('jwks',jwks)
            unverified_header = jwt.get_unverified_header(token)
            print('unverified_header',unverified_header)
            rsa_key = {}

            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"]
                    }
            if rsa_key:
                try:
                    payload = jwt.decode(
                        token,
                        rsa_key,
                        algorithms=ALGORITHMS,
                        audience=API_AUDIENCE,
                        issuer="https://"+AUTH0_DOMAIN+"/"
                    )
                except Exception:
                    return None
                return payload
        except Exception as identifier:
            return None
        pass
        
    def local_auth(token):
        try:
            return client.userinfo(token)
        except Exception as identifier:
            return None
        pass

    return prod_auth if is_prod else local_auth

auth_user = build_auth_function()