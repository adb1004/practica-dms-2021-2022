from dms2122backend.data.db import Schema 
from dms2122backend.data.db.results import Answer
from dms2122backend.logic.logicanswer import LogicAnswer
from dms2122backend.data.rest.authservice import AuthService
from typing import List, Optional, Dict
from sqlalchemy.orm.session import Session 

# Class that manages the service of the answers
class AnswersServices():

    # Answers a question
    @staticmethod
    def answer(auth_service: AuthService, username: str, id: int, qid: int, schema: Schema, token_info: Dict) -> Dict:
        o: Dict = {}
        session: Session = schema.new_session()
        try:
            ans = LogicAnswer.create(auth_service, session, username, id, qid,token_info)
            if ans is not None:
                o['qid'] = ans.qid
                o['username'] = ans.user
                o['id'] = ans.id

        except Exception as exception: raise exception
        finally: schema.remove_session()
        return o

    # All answers from a particular user
    @staticmethod
    def answerListFromUser(username: str, schema: Schema) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()
        
        try:
            answers: List[Answer] = LogicAnswer.answerListFromUser(session, username)
            for a in answers:
                o.append({'qid': a.qid, 'username': a.user, 'id': a.id})
        except Exception as exception: raise exception
        finally: schema.remove_session()
        return o

    # All answers from a particular question
    @staticmethod
    def answerListFromQuestion(qid: int, schema: Schema) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()
        
        try:
            answers: List[Answer] = LogicAnswer.answerListFromQuestion(session, questionId)
            for a in answers:
                o.append({'qid': a.qid, 'username': a.user, 'id': a.id})
        except Exception as exception: raise exception
        finally: schema.remove_session()
        return o

    # Gets if a question has an answer
    @staticmethod
    def questionHasAnswers(auth_service: AuthService, token_info: Dict, qid: int, schema: Schema) -> bool:
        session: Session = schema.new_session()
        
        try:
            answer: bool = LogicAnswer.questionHasAnswers(auth_service,token_info,session, qid)
        except Exception as exception: raise exception
        finally: schema.remove_session()
        return answer 
    
    # Returns an answer from a particular user to a particular question
    @staticmethod
    def answerFromUserToQuestion(user: str, qid: int, schema: Schema) -> Dict:
        o: Dict = {}
        session: Session = schema.new_session()
        
        try:
            answer: Answer = LogicAnswer.answerFromUserToQuestion(session, user, qid)
            if answer is not None:
                o['qid'] = answer.qid
                o['username'] = answer.user
                o['id'] = answer.id
        except Exception as exception: raise exception
        finally: schema.remove_session()
        return o 

    # Returs the puntuation from a particular answer
    @staticmethod
    def answerScore(answer: Answer, schema: Schema) -> Optional[float]:
        session: Session = schema.new_session()   
        score: Optional[float] = 0     
        
        try:
            if score is None: return None

            score = LogicAnswer.answerScore(session, answer)
            return score
        except Exception as exception: raise excepton
        finally: schema.remove_session()
    
    # Returns all the answers
    @staticmethod
    def allAnswers(schema: Schema) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()
        answers: List[Answer] = LogicAnswer.allAnswers(session)
        
        for a in answers:
            o.append({'qid': a.id, 'id': a.number, 'user': a.user})
        schema.remove_session()
        
        return o