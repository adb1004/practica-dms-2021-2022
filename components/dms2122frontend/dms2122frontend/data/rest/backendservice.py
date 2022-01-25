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

    # Base url
    def __base_url(self) -> str:
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'

    # All the questions
    def list_questions(self, token: Optional[str]) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(self.__base_url() + '/questions',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret}
        )

        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

    # Method that creates a question
    def create_question(self, token: Optional[str], title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.post(
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
        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
        
        return rp_data

    # Question from its questions id
    def get_question(self, token: Optional[str], qid: int) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/question/{qid}',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret}
        )
        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

    # Returns if a particular question has any answer
    def questionHasAnswers(self, token: Optional[str], qid: int) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/question/{qid}/ans',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret})

        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

    # Answers a question
    def answer_question(self, token: Optional[str], qid: int, id: int, username: str) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.post(
            self.__base_url() + f'/question/{qid}/ans/{username}',
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
        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
         
        return rp_data

    # All answers from a particular question
    def allAnswersFromQuestion(self, token: Optional[str], qid: int) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/answers/{qid}',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            }
        )
        rp_data.set_successful(rp.ok)
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        return rp_data

    # All answers from a particular user
    def allAnswersFromUsername(self, token: Optional[str], username: str) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/answers/{username}',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            }
        )

        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])

        return rp_data 

    # Modifies a particular question
    def modify_question(self, token: Optional[str], qid: int, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.put(
            self.__base_url() + f'/question/{qid}',
            json={
                'qid': qid,
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
                self.__apikey_header: self.__apikey_secret
            }
        )
        rp_data.set_successful(rp.ok)
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
        return rp_data

    # Returns a particular answer
    def get_answer(self, token: Optional[str], username: str, qid: int) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/question/{qid}/ans/{username}',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            }
        )
        rp_data.set_successful(rp.ok)

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])

        return rp_data
    
    # All incompleted questions from a particular user
    def questionsIncompletedFromUser(self, token: Optional[str], username: str) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        
        rp: requests.Response = requests.get(
            self.__base_url() + f'/questions/{username}/incompleted',
            headers={'Authorization': f'Bearer {token}', self.__apikey_header: self.__apikey_secret}
        )
        
        rp_data.set_successful(rp.ok)
        
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

    # All completed questions from a particular user
    def questionsCompletedFromUser(self, token: Optional[str], username: str) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        
        rp: requests.Response = requests.get(
            self.__base_url() + f'/questions/{username}/completed',
            headers={'Authorization': f'Bearer {token}', self.__apikey_header: self.__apikey_secret}
        )
        
        rp_data.set_successful(rp.ok)
        
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

    # All statistics from a particular user
    def userStatistics(self, token: Optional[str], username: str) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/statistics/{username}',
            headers={'Authorization': f'Bearer {token}', self.__apikey_header: self.__apikey_secret}
        )
        rp_data.set_successful(rp.ok)
        
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

    # All statistics from a particular question
    def questionStatistics(self, token: Optional[str]) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/statistics/questions',
            headers={'Authorization': f'Bearer {token}', self.__apikey_header: self.__apikey_secret}
        )
        rp_data.set_successful(rp.ok)
        
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data

    # All statistics from all users
    def usersStatistics(self, token: Optional[str]) -> ResponseData:
        rp_data: ResponseData = ResponseData()
        rp: requests.Response = requests.get(
            self.__base_url() + f'/statistics/users',
            headers={'Authorization': f'Bearer {token}', self.__apikey_header: self.__apikey_secret}
        )
        rp_data.set_successful(rp.ok)
        
        if rp_data.is_successful():
            rp_data.set_content(rp.json())
        else:
            rp_data.add_message(rp.content.decode('ascii'))
            rp_data.set_content([])
        
        return rp_data