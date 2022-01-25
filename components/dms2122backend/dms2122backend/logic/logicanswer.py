from dms2122backend.data.rest import AuthService
from dms2122backend.data.db.results import Answer
from dms2122backend.data.db.results import Question
from dms2122backend.data.db.resultsets import Questions
from dms2122backend.data.db import Schema 
from dms2122backend.data.db.resultsets import Answers
from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session

# Class that manages the logic behind the answers
class LogicAnswer():
    
    # Creates a answer
    @staticmethod
    def create(auth_service: AuthService, session: Session, user: str, id: int, qid: int, token_info: Dict) -> Answer:
        try:
            nAnswer: Answer = Answers.answer(session, user, id, qid)
        except Exception as exception: raise exception
        return nAnswer

    # All the answers from a particular user
    @staticmethod
    def answerListFromUser(session: Session,user: str) -> List[Answer]:
        try:
            return Answers.answerListFromUser(session, user)
        except Exception as exception: raise exception

    # All the answers from a particular question
    @staticmethod
    def answerListFromQuestion(session: Session,qid: int) -> List[Answer]:
        try:
            return Answers.answerListFromQuestion(session, qid)
        except Exception as exception: raise exception

    # Returns if a particular question has answers
    @staticmethod
    def questionHasAnswers(auth_service: AuthService, token_info: Dict,session: Session, qid: int) -> bool:
        rp: ResponseData = auth_service.get_user_has_role(session.get('token'), token_info['user_token']['user'], "Teacher")
        if rp.is_successful() == False:
            raise NotValidOperation
        
        try:
            return Answers.questionHasAnswers(session,qid)
        except Exception as exception: raise exception

    # Answer from a particular user to a particular question
    @staticmethod
    def answerFromUserToQuestion(session: Session ,user: str, id: int) -> Answer:
        try:
            answer: Answer = Answers.answerFromUserToQuestion(session,user,id)
        except Exception as exception: raise exception
        
        return answer

    # Puntuation from an answer
    @staticmethod
    def answerScore(session: Session, answer: Answer) -> float:
        try:
            q: Question = Questions.getQuestionFromId(session, answer.qid)
            if q is None: return None

            if q.c_right==answer.id:
                return q.puntuation
            else: return q.penalization

        except Exception as exception: raise exception

    # All the answers
    @staticmethod
    def allAnswers(session: Session) -> List[Answer]:
        query = session.query(Answer)
        return query.all()