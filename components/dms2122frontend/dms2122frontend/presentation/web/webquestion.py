from dms2122common.data.rest import ResponseData
from dms2122frontend.data.rest.backendservice import BackendService
from typing import Dict, List, Optional
from flask import session
from .webutils import WebUtils


class WebQuestion():
    @staticmethod
    def list_questions(backend_service: BackendService) -> List:
        response: ResponseData = backend_service.list_questions(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []
    
    @staticmethod
    def create_question(backend_service: BackendService, title: str,  desc: str, c_1: str, c_2: str,c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> Optional[Dict]:
        response: ResponseData = backend_service.create_question(session.get('token'), title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def get_question(backend_service: BackendService, qid: int) -> Optional[Dict]:
        response: ResponseData = backend_service.get_question(session.get('token'), qid)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def modify_question(backend_service: BackendService, qid: int, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4 : str, c_right: int, puntuation: float, penalization: float) -> Optional[Dict]:
        response: ResponseData = backend_service.modify_question(session.get('token'), qid, title, desc, c_1, c_2, c_3, c_right, puntuation, penalization)
        WebUtils.flash_response_messages(response)
        return response.get_content()

    @staticmethod
    def questionHasAnswers(backend_service: BackendService, qid: int) -> bool:
        response: ResponseData = backend_service.questionHasAnswers(session.get('token'), qid)
        WebUtils.flash_response_messages(response)
        return response.is_successful()