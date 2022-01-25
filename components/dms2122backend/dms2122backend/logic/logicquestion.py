from dms2122backend.data.rest import AuthService
from dms2122backend.data.db.results import Answer
from dms2122backend.data.db.resultsets import Answers
from dms2122backend.logic.logicanswer import LogicAnswer
from dms2122backend.data.db import Schema 
from dms2122backend.data.db.results import Question, answer
from dms2122backend.data.db.resultsets import Questions
from dms2122backend.logic.exc.notvalidoperation import NotValidOperation
from dms2122common.data.rest import ResponseData
from typing import List, Optional, Dict
from sqlalchemy.orm.session import Session  

class LogicQuestion():
    @staticmethod
    def create(auth_service: AuthService, token_info: Dict, session: Session, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> Optional[Question]:       
        try:
            nQuestion: Question = Questions.create(session, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
        except Exception as exception:
            raise exception
       
        return nQuestion

    @staticmethod
    def questionsList(session: Session) -> List[List]:
        questionsList : List[List] = []
        questions = Questions.questionsList(session)
        
        for q in questions:
            if (Answers.questionHasAnswers(session, q.qid)): questionsList.append([q, 1])
            else: questionsList.append([q, 0])
        
        return questionsList

    @staticmethod
    def getQuestionFromId(session: Session, qid: int,) -> Optional[Question]:
        try:
            question = Questions.getQuestionFromId(session, qid)
        except Exception as exception: raise exception
        
        return question

    @staticmethod
    def modify(auth_service: AuthService, token_info: Dict, session: Session, qid: int, title: str,  desc: str, c_1: str, c_2: str, c_3: str, c_4: str, c_right: int, puntuation: float, penalization: float) -> Question:
        try:
            question = Questions.modify(session, qid, title, desc, c_1, c_2, c_3, c_4, c_right, puntuation, penalization)
        except Exception as exception: raise exception
        
        return question

    @staticmethod
    def questionsIncompletedFromUser(session: Session, user: str) -> List[Question]:
        try:
            questions = Questions.questionsList(session)
            incompleted = []
            
            for q in questions:
                if Answers.answerFromUserToQuestion(session, user, q.qid) is None:
                    incompleted.append(q)
        
        except Exception as exception: raise exception
        return incompleted

    @staticmethod
    def questionsCompletedFromUser(session: Session, user: str) -> List[List]:
        try:
            completed: List[List] = []
            questions = Questions.questionsList(session)
            
            for q in questions:
                a = Answers.answerFromUserToQuestion(session, user, q.qid)
                if Answers.answerFromUserToQuestion(session, user, q.qid) is not None:
                    score = LogicAnswer.answerScore(session, a)
                    completed.append([q,score])
        
        except Exception as exception: raise exception
        return completed