from dms2122backend.data.db import Schema 
from dms2122backend.data.db.results import Answer
from dms2122backend.logic.logicanswer import LogicAnswer
from dms2122backend.data.rest.authservice import AuthService
from typing import List, Dict
from sqlalchemy.orm.session import Session 


class AnswersServices():
    @staticmethod
    def answer(auth_service: AuthService, token_info: Dict, username: str, id: int, qid: int, schema: Schema) -> None:
        session: Session = schema.new_session()
        try:
            LogicAnswer.create(auth_service,token_info, session, username, id, qid)

        except Exception as exception:
            raise exception
        finally:
            schema.remove_session()

    @staticmethod
    def answerListFromUser(username: str, schema: Schema) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()
        answers: List[Answer] = LogicAnswer.answerListFromUser(session, username)
        for a in answers:
            o.append({'qid': a.qid, 'username': a.user, 'id': a.id})
        schema.remove_session()
        return o


    @staticmethod
    def answerListFromQuestion(qid: int, schema: Schema) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()
        answers: List[Answer] = LogicAnswer.answerListFromQuestion(session, questionId)
        for a in answers:
            o.append({'qid': a.qid, 'username': a.user, 'id': a.id})
        schema.remove_session()
        return o

    @staticmethod
    def questionHasAnswers(auth_service: AuthService, token_info: Dict, qid: int, schema: Schema) -> bool:
        session: Session = schema.new_session()
        answer: bool = LogicAnswer.questionHasAnswers(auth_service,token_info,session, qid)
        schema.remove_session()
        return answer 
    
    @staticmethod
    def answerFromUserToQuestion(user: str, qid: int, schema: Schema) -> Dict:
        o: Dict = {}
        session: Session = schema.new_session()
        answer: Answer = LogicAnswer.answerFromUserToQuestion(session, user, qid)
        out['qid'] = answer.qid
        out['username'] = answer.user
        out['id'] = answer.id
        schema.remove_session()
        return o 