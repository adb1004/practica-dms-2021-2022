from typing import  Dict, List, Optional
from dms2122backend.data.db import Schema 
from dms2122backend.data.db.results import Question
from dms2122backend.data.db.resultsets import Questions
from sqlalchemy.orm.session import Session

class QuestionsService():

    @staticmethod
    def get_question(title:str, desc:str, c_1:str, c_2:str, c_3:str, c_4:str, c_right:int, puntuation: float, penalization: float, schema: Schema)-> Optional[Question]:
        session: Session = schema.new_session()
        questionFound = Questions.get_question(session, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
        schema.remove_session()
        return questionFound

    @staticmethod
    def getQuestionFromId( id: int, schema: Schema)-> Optional[Question]:
        session: Session = schema.new_session()
        questionFound = Questions.getQuestionFromId(session, id)
        schema.remove_session()
        return questionFound

    @staticmethod
    def list_questions(schema: Schema) -> List[Dict]:
        out: List[Dict] = []
        session: Session = schema.new_session()
        questions: List[Question] = Questions.questionsList(session)
        
        for q in questions:
            out.append({'title': q.title})
        schema.remove_session()
        return out

    @staticmethod
    def create_question(title:str, desc:str, c_1:str, c_2:str, c_3:str, c_4:str, c_right:int, puntuation: float, penalization: float, schema: Schema) -> Dict:
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            nQuestion: Question = Questions.create(session, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
            out['title'] = nQuestion.title
        except Exception as exception:
            raise exception
        finally:
            schema.remove_session()
        return out