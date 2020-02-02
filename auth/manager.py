from keycloak.realm import KeycloakRealm
from keycloak.openid_connect import KeycloakOpenidConnect

from configuration.manager import ConfigurationManager, ConfigProp

class AuthServer:
    __server = {}
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def create_connection_client(self, client_id, client_secret) -> KeycloakOpenidConnect:
        return self.__get_server().open_id_connect(client_id, client_secret)

    def __get_server(self) -> KeycloakRealm:
        server = self.__server.get('server', None)
        if server is None:
            server_url = ConfigurationManager.get_config_value(ConfigProp.auth_server_url())
            server_realm = ConfigurationManager.get_config_value(ConfigProp.auth_env())
            self.__server.update({'server':KeycloakRealm(server_url=server_url, realm_name=server_realm)})
            server = self.__server.get('server', None)
        return server

    

