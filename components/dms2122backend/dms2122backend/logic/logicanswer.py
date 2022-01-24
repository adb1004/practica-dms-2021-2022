from dms2122backend.data.rest import AuthService
from dms2122backend.data.db.results import Answer
from dms2122backend.data.db import Schema 
from dms2122backend.data.db.resultsets import Answers
from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session


class LogicAnswer():
    @staticmethod
    def create(auth_service: AuthService, token_info: Dict, session: Session, user: str, id: int, qid: int) -> Answer:
        rp: ResponseData = auth_service.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Student")
        if rp.is_successful() == False:
            raise NotValidOperation
        try:
            nAnswer: Answer = Answers.answer(session, user, id, qid)
        except Exception as exception:
            raise exception
        return nAnswer

    @staticmethod
    def answerListFromUser(session: Session,user: str) -> List[Answer]:
        return Answers.answerListFromUser(session, user)

    @staticmethod
    def answerListFromQuestion(session: Session,qid: int) -> List[Answer]:
        return Answers.answerListFromQuestion(session, qid)

    @staticmethod
    def questionHasAnswers(auth_service: AuthService, token_info: Dict,session: Session, qid: int) -> bool:
        rp: ResponseData = auth_service.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if rp.is_successful() == False:
            raise NotValidOperation
        return Answers.questionHasAnswers(session,qid)

    @staticmethod
    def answerFromUserToQuestion(session: Session ,user: str, id: int) -> Answer:
        try:
            answer: Answer = Answers.answerFromUserToQuestion(session,user,id)
        except Exception as exception:
            raise exception
        return answer