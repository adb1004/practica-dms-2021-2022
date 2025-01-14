from dms2122backend.logic import LogicQuestion
from dms2122backend.data.db import Schema 
from dms2122backend.data.rest import AuthService
from dms2122backend.data.db.results import Question
from typing import  Dict, List, Optional
from sqlalchemy.orm.session import Session

# Class that manages the service of the questions
class QuestionsService():

    # Returns a question from its question id
    @staticmethod
    def getQuestionFromId(qid: int, schema: Schema)-> Dict:
        session: Session = schema.new_session()
        o: Dict = {}
        try:
            question = LogicQuestion.getQuestionFromId(session, qid)
            if question is not None:
                o['qid'] = question.qid
                o['title'] = question.title
                o['desc'] = question.desc
                o['c_1'] = question.c_1
                o['c_2'] = question.c_2
                o['c_3'] = question.c_3
                o['c_4'] = question.c_4
                o['c_right'] = question.c_right
                o['puntuation'] = question.puntuation
                o['penalization'] = question.penalization
        except Exception as exception:
            raise exception
        finally:
            schema.remove_session()

        return o

    # All the questions
    @staticmethod
    def list_questions(schema: Schema) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()
        questions: List[List] = LogicQuestion.questionsList(session)
        for particularQuestion in questions:
            q: Question = particularQuestion[0]
            completed: int = particularQuestion[1]
            o.append({'qid': q.qid, 'title': q.title, 'desc': q.desc, 'c_1': q.c_1, 'c_2': q.c_2, 'c_3': q.c_3, 'c_4': q.c_4, 'c_right': q.c_right, 'puntuation': q.puntuation, 'penalization': q.penalization, 'completed' : completed})
        schema.remove_session()
        return o

    # Method that creates a question
    @staticmethod
    def create_question(auth_service: AuthService, token_info: Dict, title:str, desc:str, c_1:str, c_2:str, c_3:str, c_4:str, c_right:int, puntuation: float, penalization: float, schema: Schema) -> Dict:
        session: Session = schema.new_session()
        o: Dict = {}
        try:
            nQuestion: Question = LogicQuestion.create(auth_service, token_info, session, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
            o['qid'] = nQuestion.qid
            o['title'] = nQuestion.title
            o['desc'] = nQuestion.desc
            o['c_1'] = nQuestion.c_1
            o['c_2'] = nQuestion.c_2
            o['c_3'] = nQuestion.c_3
            o['c_4'] = nQuestion.c_4
            o['c_right'] = nQuestion.c_right
            o['puntuation'] = nQuestion.puntuation
            o['penalization'] = nQuestion.penalization
        except Exception as exception:
            raise exception
        finally:
            schema.remove_session()
        return o
    
    # Method that modifies an existing question
    @staticmethod
    def modify_question(auth_service: AuthService, token_info: Dict, qid: int, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float, schema: Schema) -> Optional[Question]:
        session: Session = schema.new_session()
        o: Dict = {}
        try:
            nQuestion = LogicQuestion.modify(auth_service, token_info, session, qid, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
            o['qid'] = nQuestion.qid
            o['title'] = nQuestion.title
            o['desc'] = nQuestion.desc
            o['c_1'] = nQuestion.c_1
            o['c_2'] = nQuestion.c_2
            o['c_3'] = nQuestion.c_3
            o['c_4'] = nQuestion.c_4
            o['c_right'] = nQuestion.c_right
            o['puntuation'] = nQuestion.puntuation
            o['penalization'] = nQuestion.penalization
        except Exception as exception:
            raise exception
        finally:
            schema.remove_session()
        return o

    # All the questions incompleted from a particular user
    @staticmethod
    def questionsIncompletedFromUser(schema: Schema, user: str) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()

        try:
            questions: List[Question] = LogicQuestion.questionsIncompletedFromUser(session, user)
            for q in questions:
                o.append({'qid': q.qid, 'title': q.title, 'desc': q.desc, 'c_1': q.c_1, 'c_2': q.c_2, 'c_3': q.c_3, 'c_4': q.c_4, 'c_right': q.c_right, 'puntuation': q.puntuation, 'penalization': q.penalization})
        except Exception as exception: raise exception
        finally: schema.remove_session()
        return o

    # All the questions completed from a particular user
    @staticmethod
    def questionsCompletedFromUser(schema: Schema, user: str) -> List[Dict]:
        o: List[Dict] = []
        session: Session = schema.new_session()
        
        try:
            questions: List[List] = LogicQuestion.questionsCompletedFromUser(session, user)
            for qLs in questions:
                q: Question = qLs[0]
                puntuation: float = qLs[1] 
                o.append({'qid': q.qid, 'title': q.title, 'desc': q.desc, 'c_1': q.c_1, 'c_2': q.c_2, 'c_3': q.c_3, 'c_4': q.c_4, 'c_right': q.c_right, 'puntuation': q.puntuation, 'penalization': q.penalization, 'result': puntuation})
        except Exception as exception: raise exception
        finally: schema.remove_session()
        return o