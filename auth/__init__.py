
from auth.manager import AuthServer

from configuration.manager import ConfigurationManager, ConfigProp

# realm = KeycloakRealm(server_url='http://localhost:8080', realm_name='dev')

# client = realm.open_id_connect('omt-server','a9433638-d008-409e-9a27-6b6c20a5e02e' )

server = AuthServer()

client = server.create_connection_client(ConfigurationManager.get_config_value(ConfigProp.auth_client_id()),ConfigurationManager.get_config_value(ConfigProp.auth_client_secret()))

def auth_user(token):
    try:
        return client.userinfo(token)
    except Exception as identifier:
        return None
    pass