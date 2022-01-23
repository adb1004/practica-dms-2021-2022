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
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + f'/user/{username}/role/{rolename}',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            }
        )

        response_data.set_successful(response.ok)

        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
            response_data.set_content([])

        return response_data

    def __base_url(self) -> str:
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'