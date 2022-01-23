from typing import Dict
from dms2122common.data.config import ServiceConfiguration

class BackendConfiguration(ServiceConfiguration):

    def _component_name(self) -> str:
        return 'dms2122backend'

    def __init__(self):
        
        ServiceConfiguration.__init__(self)

        self.set_db_connection_string('sqlite:////tmp/dms2122backend.sqlite3.db')
        self.set_service_host('127.0.0.1')
        self.set_service_port(5000)
        self.set_debug_flag(True)
        self.set_password_salt('This salt should be changed ASAP')
        self.set_authorized_api_keys([])
        self.set_auth_service({
            'host': '127.0.0.1',
            'port': 4000,
            'apikey_secret': 'This should be the backend API key'
        })


    def _set_values(self, values: Dict) -> None:
        ServiceConfiguration._set_values(self, values)

        if 'db_connection_string' in values:
            self.set_db_connection_string(values['db_connection_string'])

        if 'salt' in values:
            self.set_password_salt(values['salt'])

        if 'auth_service' in values:
            self.set_auth_service(values['auth_service'])

    def get_db_connection_string(self) -> str:
        return str(self._values['db_connection_string'])

    def set_db_connection_string(self, db_connection_string: str) -> None:
        self._values['db_connection_string'] = str(db_connection_string)

    def get_password_salt(self) -> str:
        return str(self._values['salt'])

    def set_password_salt(self, salt: str) -> None:
        self._values['salt'] = str(salt)

    def get_auth_service(self) -> Dict:
        return self._values['auth_service']

    def set_auth_service(self, auth_service: Dict) -> None:
        self._values['auth_service'] = auth_service