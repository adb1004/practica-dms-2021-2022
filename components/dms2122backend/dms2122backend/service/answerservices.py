from dms2122backend.data.db import Schema 
from dms2122backend.data.db.results import Answer
from dms2122backend.data.db.resultsets import Answers
from typing import List, Dict
from sqlalchemy.orm.session import Session 


class AnswersServices():
    @staticmethod
    def answer(username: str, id: int, qid: int, schema: Schema) -> None:
        session: Session = schema.new_session()
        try:
            Answers.answer(session, username, id, qid)

        except Exception as exception:
            raise exception
        finally:
            schema.remove_session()

    @staticmethod
    def answerListFromUser(username: str, schema: Schema) -> List[Answer]:
        session: Session = schema.new_session()
        answer = Answers.list_all_for_user(session, username)
        schema.remove_session()
        return answer


    @staticmethod
    def answerListFromQuestion(qid: int, schema: Schema) -> List[Answer]:
        session: Session = schema.new_session()
        answer = Answers.list_all_for_question(session, qid)
        schema.remove_session()
        return answer

    @staticmethod
    def questionHasAnswers(qid: int, schema: Schema) -> bool:
        session: Session = schema.new_session()
        answer = Answers.question_has_answers(session, questionId)
        schema.remove_session()
        return answer 
    
    @staticmethod
    def answerFromUserToQuestion(user: str, qid: int, schema: Schema) -> Answer:
        session: Session = schema.new_session()
        answer = Answers.answerFromUserToQuestion(session, user, qid)
        schema.remove_session()
        return answer 