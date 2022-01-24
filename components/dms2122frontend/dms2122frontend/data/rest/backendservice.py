from typing import Optional
import requests
from dms2122common.data import Role
from dms2122common.data.rest import ResponseData


class BackendService():
    """ REST client to connect to the backend service.
    """

    def __init__(self,
        host: str, port: int,
        api_base_path: str = '/api/v1',
        apikey_header: str = 'X-ApiKey-Backend',
        apikey_secret: str = ''
        ):
        """ Constructor method.

        Initializes the client.

        Args:
            - host (str): The backend service host string.
            - port (int): The backend service port number.
            - api_base_path (str): The base path that is prepended to every request's path.
            - apikey_header (str): Name of the header with the API key that identifies this client.
            - apikey_secret (str): The API key that identifies this client.
        """
        self.__host: str = host
        self.__port: int = port
        self.__api_base_path: str = api_base_path
        self.__apikey_header: str = apikey_header
        self.__apikey_secret: str = apikey_secret

    def __base_url(self) -> str:
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'

    def list_questions(self, token: Optional[str]) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(self.__base_url() + '/questions',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret}
        )

        response_data.set_successful(response.ok)

        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
            response_data.set_content([])
        
        return response_data

    def create_question(self, token: Optional[str], title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.post(
            self.__base_url() + '/question/create',
            json={
                'title': title,
                'desc': desc,
                'c_1': c_1,
                'c_2': c_2,
                'c_3': c_3,
                'c_4': c_4,
                'c_right': c_right,
                'puntuation': puntuation,
                'penalization': penalization
            },
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret}
        )
        response_data.set_successful(response.ok)

        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
        
        return response_data

    def get_question(self, token: Optional[str], qid: int) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + f'/question/{qid}',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret}
        )
        response_data.set_successful(response.ok)

        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
            response_data.set_content([])
        
        return response_data


    def questionHasAnswers(self, token: Optional[str], qid: int) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + f'/question/{qid}/ans',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret})

        response_data.set_successful(response.ok)

        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
            response_data.set_content([])
        
        return response_data

    def answer_question(self, token: Optional[str], qid: int, id: int, username: str) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.post(
            self.__base_url() + f'/question/{qid}/ans{username}',
            json={
                'username': username,
                'id': id,
                'qid': qid
            },
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
         
        return response_data

    def allAnswersFromQuestion(self, token: Optional[str], qid: int) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + f'/answers/{qid}',
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

    def allAnswersFromUsername(self, token: Optional[str], username: str) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + f'/answers/{username}',
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

    def modify_question(self, token: Optional[str], qid: int, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.post(
            self.__base_url() + f'/question/{qid}',
            json={
                'qid': qid,
                'title': title,
                'desc': desc,
                'c_1': c_1,
                'c_2': c_2,
                'c_3': c_3,
                'c_4': c_4,
                'c_right': correct_answer,
                'puntuation': puntuation,
                'penalization': penalization
            },
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
        return response_data

    def get_answer(self, token: Optional[str], username: str, qid: int) -> ResponseData:
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + f'/question/{qid}/ans/{username}',
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