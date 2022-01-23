from dms2122backend.data.rest.authservice import  AuthService
from dms2122backend.data.db.exc import QuestionAlreadyExist
from dms2122backend.service import QuestionsService
from dms2122backend.data.db.results import Question
from dms2122common.data.rest import ResponseData
from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app, session


def list_questions() -> Tuple[List[Dict], Optional[int]]:
    with current_app.app_context():
        questions: List[Dict] = QuestionsService.list_questions(current_app.db)
    return (questions, HTTPStatus.OK.value)

def create_question(authservice: AuthService, body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        response: ResponseData = authservice.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if response.is_successful() == False:
            return (
                'This user does not have enough privileges to create a new question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            question: Dict = QuestionsService.create_question(
                body['title'], body['desc'],  body['c_1'], body['c_2'], body['c_3'], body['c_4'], body['c_right'], body['puntuation'],body['penalization'],current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)
        except QuestionAlreadyExist:
            return ('That title is used by another question', HTTPStatus.CONFLICT.value)
    return (question, HTTPStatus.OK.value)

def get_question(authservice: AuthService, body: Dict, token_info: Dict) -> Tuple[Union[Optional[Question], str], Optional[int]]:
    with current_app.app_context():
        response: ResponseData = authservice.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if response.is_successful() == False:
            return (
                'This user does not have enough privileges to create a new question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            question = QuestionsService.get_question(
                body['title'], body['desc'],  body['c_1'], body['c_2'], body['c_3'], body['c_4'], body['c_right'], body['puntuation'],body['penalization'],current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (question, HTTPStatus.OK.value)

def get_question_by_id(authservice: AuthService, qid: int, token_info: Dict) -> Tuple[Union[Optional[Question], str], Optional[int]]:
    with current_app.app_context():
        try:
            question = QuestionsServices.get_question_by_id(
                qid, current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (question, HTTPStatus.OK.value)

def modify_question(authservice: AuthService, body: Dict, qid: int, token_info: Dict):
    with current_app.app_context():
        response: ResponseData = authservice.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if response.is_successful() == False:
            return (
                'This user does not have enough privileges to create a new question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            question = QuestionsServices.edit_question(
                id, body['title'], body['desc'],  body['c_1'], body['c_2'], body['c_3'], body['c_4'], body['c_right'], body['puntuation'],body['penalization'],current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value) 
        except QuestionOrUserNotCreated:
            return ('The question or the user does not been created', HTTPStatus.NOT_FOUND.value)       
    return (question, HTTPStatus.OK.value)