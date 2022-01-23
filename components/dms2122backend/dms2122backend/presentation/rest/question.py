from dms2122auth.service.roleservices import  RoleServices
from dms2122backend.data.db.exc import QuestionExistsError
from dms2122backend.service import QuestionsService
from dms2122common.data.role import Role
from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app


def list_questions() -> Tuple[List[Dict], Optional[int]]:
    with current_app.app_context():
        questions: List[Dict] = QuestionsService.list_questions(current_app.db)
    return (questions, HTTPStatus.OK.value)

def create_question(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        if not RoleServices.has_role(token_info['user_token']['user'], Role.Teacher, current_app.db):
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

def get_question(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        if not RoleServices.has_role(token_info['user_token']['user'], Role.Teacher, current_app.db):
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

def get_question_by_id(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        if not RoleServices.has_role(token_info['user_token']['user'], Role.Teacher, current_app.db):
            return (
                'This user does not have enough privileges to create a new question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            question: Dict = QuestionsService.get_question(
                body['qid'], current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (question, HTTPStatus.OK.value)