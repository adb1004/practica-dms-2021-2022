import hashlib
from dms2122backend.data.db.results import Answer
from dms2122backend.data.db.exc.questionorusernotcreated import QuestionOrUserNotCreated
from dms2122backend.data.db.exc import UserNotRegistered
from sqlalchemy.exc import IntegrityError  
from sqlalchemy.orm.exc import NoResultFound  
from sqlalchemy.orm.session import Session
from typing import List

# Class that represents all the answeres
class Answers():
    
    # Method that creates and register an answer
    @staticmethod
    def answer(session: Session, username: str, qid: str, id: int) -> Answer:
        if not username or not qid or not id:
            raise ValueError('At least 1 field is not completed')
        try:
            nAnswer = Answer(username, id, qid)
            session.add(nAnswer)
            session.commit()
            return nAnswer
        except IntegrityError as exception:
            session.rollback()
            raise QuestionOrUserNotCreated() from exception 
        except:
            session.rollback()
            raise
    
    # All the answers from a particular user
    @staticmethod
    def answerListFromUser(session: Session, user: str) -> List[Answer]:
        if not user:
            raise ValueError('User is empty')
        
        query = session.query(Answer).filter_by(user=user)
        return query.all()

    # All the answers from a particular question
    @staticmethod
    def answerListFromQuestion(session: Session, qid: int) -> List[Answer]:
        if not qid:
            raise ValueError('qid is empty')

        query = session.query(Answer).filter_by(qid=qid)
        return query.all()

    # If a questions has answers
    @staticmethod
    def questionHasAnswers(session: Session, qid: int) -> bool:
        if not qid:
            raise ValueError('qid is empty')

        questions = Answers.answerListFromQuestion(session, qid)

        return len(questions) != 0 

    # Tne answer of a particular user to a particular question
    @staticmethod
    def answerFromUserToQuestion(session: Session, user: str, qid: int) -> Answer:
        if not user:
            raise ValueError('Username is empty')
        query = session.query(Answer).filter_by(
            user=user, qid=qid
        )
        return query.one_or_none() 

    # All the answers
    @staticmethod
    def allAnswers(session: Session) -> List[Answer]:
        query = session.query(Answer)
        return query.all()

