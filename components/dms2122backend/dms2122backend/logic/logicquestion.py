from dms2122backend.data.rest import AuthService
from dms2122backend.data.db import Schema 
from dms2122backend.data.db.results import Question
from dms2122backend.data.db.resultsets import Questions
from dms2122backend.logic.exc.notvalidoperation import NotValidOperation
from dms2122common.data.rest import ResponseData
from typing import List, Optional, Dict
from sqlalchemy.orm.session import Session  

class LogicQuestion():
    @staticmethod
    def create(auth_service: AuthService, token_info: Dict, session: Session, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> Optional[Question]:
        rp: ResponseData = auth_service.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        
        if rp.is_successful() == False: raise ForbiddenOperationError
        
        try:
            nQuestion: Question = Questions.create(session, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
        except Exception as exception:
            raise exception
       
        return nQuestion

    @staticmethod
    def questionsList(session: Session) -> List[Question]:
        return Questions.questionsList(session)

    @staticmethod
    def getQuestionFromId(session: Session, qid: int,) -> Optional[Question]:
        try:
            question = Questions.getQuestionFromId(session, qid)
        except Exception as exception:
            raise exception
        
        return question

    @staticmethod
    def modify(auth_service: AuthService, token_info: Dict, session: Session, qid: int, title: str,  desc: str, c_1: str, c_2: str,
             c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> Question:
        rp: ResponseData = auth_service.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if rp.is_successful() == False:
            raise ForbiddenOperationError
        
        try:
            question = Questions.edit(session, qid, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
        except Exception as exception:
            raise exception
        
        return question