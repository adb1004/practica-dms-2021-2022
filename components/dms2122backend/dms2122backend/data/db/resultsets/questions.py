import hashlib
from dms2122backend.data.db.results import Question
from dms2122backend.data.db.exc import QuestionAlreadyExist
from sqlalchemy.exc import IntegrityError  
from sqlalchemy.orm.exc import NoResultFound  
from sqlalchemy.orm.session import Session
from typing import List, Optional

class Questions():

    @staticmethod
    def create(session: Session, title:str, desc:str, c_1:str, c_2:str, c_3:str, c_4:str, c_right:int, puntuation: float, penalization: float) -> Question:
        if not title or not desc or not c_1 or not c_2 or not c_3 or not c_4 or not c_right or not puntuation or not penalization:
            raise ValueError('At least 1 field is not completed')
        
        try:
            new_question = Question(title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
            session.add(new_question)
            session.commit()
            return new_question
        except IntegrityError as exception:
            raise QuestionAlreadyExist('There is already a question created with te same title: ' + title) from exception
    
    @staticmethod
    def questionsList(session: Session) -> List[Question]:
        query = session.query(Question)
        return query.all()
    
    @staticmethod
    def getQuestionFromId(session: Session, qid: int,) -> Optional[Question]:
        try:
            query = session.query(Question).filter_by(qid=qid)
            question: Question = query.one()
        except NoResultFound:
            return None
        return question 
    
    @staticmethod
    def modify(session: Session, qid: int, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> Optional[Question]:
        edit_question = Questions.get_question_by_id(session, qid)
        
        if edit_question is not None:        
            edit_question.title = title
            edit_question.desc = desc
            edit_question.c_1 = c_1
            edit_question.c_2 = c_2
            edit_question.c_3 = c_3
            edit_question.c_4 = c_4
            edit_question.c_right = c_right
            edit_question.puntuation = puntuation
            edit_question.penalization = penalization

            session.commit()

            return edit_question
        
        raise QuestionOrUserNotCreated()
