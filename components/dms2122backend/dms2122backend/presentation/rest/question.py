from dms2122backend.data.rest.authservice import  AuthService
from dms2122backend.data.db.exc.questionorusernotcreated import QuestionOrUserNotCreated
from dms2122backend.logic.exc.notvalidoperation import NotValidOperation
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

def create_question(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        try:
            question: Dict = QuestionsService.create_question(
                current_app.authservice, token_info, body['title'], body['desc'],  body['c_1'], body['c_2'], body['c_3'], body['c_4'], body['c_right'], body['puntuation'],body['penalization'],current_app.db
            )
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)
        except NotValidOperation: return ('Invalid operation', HTTPStatus.FORBIDDEN.value)
        except QuestionAlreadyExist:  return ('That question already exist', HTTPStatus.CONFLICT.value)
    return (question, HTTPStatus.OK.value)

def get_question_by_id(qid: int) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        try:
            question: Dict = QuestionsService.getQuestionFromId(
                qid, current_app.db
            )
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (question, HTTPStatus.OK.value)

def modify_question(body: Dict, qid: int, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        try:
            question: Dict = QuestionsService.modify_question(
                current_app.authservice, token_info, qid, body['title'], body['desc'],  body['c_1'], body['c_2'], body['c_3'], body['c_4'], body['c_right'], body['puntuation'],body['penalization'],current_app.db
            )
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value) 
        except QuestionOrUserNotCreated: return ('The question or the user does not been created', HTTPStatus.NOT_FOUND.value)       
        except NotValidOperation: return ('Invalid operation', HTTPStatus.FORBIDDEN.value)
    return (question, HTTPStatus.OK.value)

def questionsIncompletedFromUser(username: str) -> Tuple[Union[List[Dict], str], Optional[int]]:
    with current_app.app_context():
        try:
            questions: List[Dict] = QuestionsService.questionsIncompletedFromUser(current_app.db, username)
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)   
    return (questions, HTTPStatus.OK.value)

def questionsCompletedFromUser(username: str) -> Tuple[Union[List[Dict], str], Optional[int]]:
    with current_app.app_context():
        try:
            questions: List[Dict] = QuestionsService.questionsCompletedFromUser(current_app.db, username)
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)   
    return (questions, HTTPStatus.OK.value) 