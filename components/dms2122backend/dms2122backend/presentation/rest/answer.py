from dms2122backend.data.db.exc import QuestionAlreadyExist
from dms2122backend.data.db.exc.questionorusernotcreated import QuestionOrUserNotCreated
from dms2122backend.data.db.results.answer import Answer
from dms2122backend.service import AnswersServices
from dms2122backend.data.rest.authservice import  AuthService
from dms2122common.data.role import Role
from dms2122common.data.rest import ResponseData
from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app, session

def answer(authservice: AuthService, body: Dict, token_info: Dict) -> Tuple[Optional[str], Optional[int]]:
    with current_app.app_context():
        response: ResponseData = authservice.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Student")
        if response.is_successful() == False:
            return (
                'That user can not create a question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            AnswersServices.answer(
                body['username'],  body['id'], body['qid']
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)
        except QuestionOrUserNotCreated:
            return ('That question or that user are not created', HTTPStatus.NOT_FOUND.value)
    return (None, HTTPStatus.OK.value)


def answerListFromUser(authservice: AuthService, username: str, token_info: Dict) -> Tuple[Union[List[Answer], str], Optional[int]]:
    with current_app.app_context():
        response: ResponseData = authservice.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Student")
        if response.is_successful() == False:
            return (
                'That user can not display a question',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            answer: List[Answer] = AnswersServices.answerListFromUser(
                username, current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (answer, HTTPStatus.OK.value)


def answerListFromQuestion(authservice: AuthService, qid: int, token_info: Dict) -> Tuple[Union[List[Answer], str], Optional[int]]:
    with current_app.app_context():
        response: ResponseData = authservice.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if response.is_successful() == False:
            return (
                'That user can not display a question list',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            answer: List[Answer] = AnswersServices.answerListFromQuestion(
                qid, current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (answer, HTTPStatus.OK.value)

def questionHasAnswers(authservice: AuthService, qid:int, token_info: Dict) -> Tuple[Union[bool, str], Optional[int]]:
    with current_app.app_context():
        response: ResponseData = authservice.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if response.is_successful() == False:
            return (
                'That user can not see if a question has anwers',
                HTTPStatus.FORBIDDEN.value
            )
        try:
            answer = AnswersServices.questionHasAnswers(
                qid, current_app.db
            )
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (answer, HTTPStatus.OK.value)

def answerFromUserToQuestion(username: str, qid: int) -> Tuple[Union[Answer, str], Optional[int]]:
    with current_app.app_context():
        try:
            answer: Answer = AnswersServices.answerFromUserToQuestion(
                username, qid, current_app.db
            )
        except ValueError:
            return ('A mandatory argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (answer, HTTPStatus.OK.value)