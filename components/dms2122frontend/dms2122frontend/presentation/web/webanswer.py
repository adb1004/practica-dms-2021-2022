from dms2122common.data.rest import ResponseData
from dms2122frontend.data.rest.backendservice import BackendService
from typing import Dict, List, Optional
from flask import session
from .webutils import WebUtils

class WebAnswer():
    @staticmethod
    def answer_question(backend_service: BackendService, qid: int, id: int, username: str) -> Optional[Dict]:
        response: ResponseData = backend_service.answer_question(session.get('token'), qid, id, username)
        WebUtils.flash_response_messages(response)
        
        return response.get_content()

    @staticmethod
    def allAnswersFromQuestion(backend_service: BackendService, qid: int) -> Optional[List]:
        response: ResponseData = backend_service.allAnswersFromQuestion(session.get('token'), qid)
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def allAnswersFromUsername(backend_service: BackendService, username: str) -> Optional[List]:
        response: ResponseData = backend_service.allAnswersFromUsername(session.get('token'), username)
        WebUtils.flash_response_messages(response)
        
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        
        return []

    @staticmethod
    def get_answer(backend_service: BackendService, username: str, qid: int) -> Optional[Dict]:
        response: ResponseData = backend_service.get_answer(session.get('token'), username, qid)
        WebUtils.flash_response_messages(response)
        
        return response.get_content() 