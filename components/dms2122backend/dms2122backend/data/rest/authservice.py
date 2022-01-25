from typing import List, Optional, Union
import requests
from dms2122common.data import Role
from dms2122common.data.rest import ResponseData


class AuthService():
    def __init__(self,host: str, port: int, api_base_path: str = '/api/v1', apikey_header: str = 'X-ApiKey-Auth', apikey_secret: str = ''):
        self.__host: str = host
        self.__port: int = port
        self.__api_base_path: str = api_base_path
        self.__apikey_header: str = apikey_header
        self.__apikey_secret: str = apikey_secret

    def get_user_has_role(self, token: Optional[str], username: str, rolename: str) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/user/{username}/role/{rolename}', headers={'Authorization': f'Bearer {token}', self.__apikey_header: self.__apikey_secret}
        )

        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])

        return rp_data

    def __base_url(self) -> str:
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'

    def total_users(self, token: Optional[str]) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + '/users', headers={'Authorization': f'Bearer {token}', self.__apikey_header: self.__apikey_secret}
        )
        rp_data.set_successful(rp.ok)
        
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data 