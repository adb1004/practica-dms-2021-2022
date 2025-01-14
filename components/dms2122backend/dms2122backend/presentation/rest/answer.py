from dms2122backend.data.db.exc import QuestionAlreadyExist
from dms2122backend.data.db.exc.questionorusernotcreated import QuestionOrUserNotCreated
from dms2122backend.logic.exc.notvalidoperation import NotValidOperation
from dms2122backend.data.db.results.answer import Answer
from dms2122backend.service import AnswersServices
from dms2122backend.data.rest.authservice import  AuthService
from dms2122common.data.role import Role
from dms2122common.data.rest import ResponseData
from typing import Tuple, Union, Optional, List, Dict
from http import HTTPStatus
from flask import current_app, session

# Method that answer a question
def answer(qid: int, username: str, body: Dict, token_info: Dict) -> Tuple[Union[Dict,str], Optional[int]]:
    with current_app.app_context():
        try:
            ans = AnswersServices.answer(current_app.authservice, body['username'],  body['id'], body['qid'], current_app.db, token_info)
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)
        except QuestionOrUserNotCreated:
            return ('That question or that user are not created', HTTPStatus.NOT_FOUND.value)
        except NotValidOperation:
            return ('Invalid operation', HTTPStatus.FORBIDDEN.value)
    return (ans, HTTPStatus.OK.value)


# All the answers from a particular user
def answerListFromUser(username: str) -> Tuple[Union[List[Dict], str], Optional[int]]:
    with current_app.app_context():
        try:
            answerList: List[Dict] = AnswersServices.answerListFromUser(username, current_app.db)
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (answerList, HTTPStatus.OK.value)

# All the answers from a particular question
def answerListFromQuestion(qid: int) -> Tuple[Union[List[Dict], str], Optional[int]]:
    with current_app.app_context():
        try:
            answerList: List[Dict] = AnswersServices.answerListFromQuestion(qid, current_app.db)
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (answerList, HTTPStatus.OK.value)

# All the answers of a particualar question if the user is a teacher
def questionHasAnswers(qid:int, token_info: Dict) -> Tuple[Union[bool, str], Optional[int]]:
    with current_app.app_context():
        try:
            answer = AnswersServices.questionHasAnswers(current_app.authservice, token_info, qid, current_app.db)
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)  
        except NotValidOperation:
            return ('Invalid operation', HTTPStatus.FORBIDDEN.value)      
    return (answer, HTTPStatus.OK.value)

# Answer form a particular user to a particular question
def answerFromUserToQuestion(username: str, qid: int) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        try:
            answer: Dict = AnswersServices.answerFromUserToQuestion(username, qid, current_app.db)
        except ValueError:
            return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (answer, HTTPStatus.OK.value)

# All the answers
def allAnswers() -> Tuple[List[Dict], Optional[int]]:
    with current_app.app_context():
        ans: List[Dict] = AnswersServices.allAnswers(current_app.db)
    return (ans, HTTPStatus.OK.value)