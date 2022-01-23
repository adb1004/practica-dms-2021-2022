from dms2122backend.data.db import Schema 
from dms2122backend.data.db.results import Answer
from dms2122backend.data.db.resultsets import Answers
from typing import List, Dict
from sqlalchemy.orm.session import Session 


class AnswersServices():
    @staticmethod
    def answer(username: str, id: int, qid: int, schema: Schema) -> None:
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            Answers.answer(session, username, id, qid)

        except Exception as exception:
            raise exception
        finally:
            schema.remove_session()

    @staticmethod
    def answerListFromUser(schema: Schema, username: str) -> List[Answer]:
        session: Session = schema.new_session()
        answer = Answers.list_all_for_user(session, username)
        schema.remove_session()
        return answer


    @staticmethod
    def answerListFromQuestion(schema: Schema, qid: int) -> List[Answer]:
        session: Session = schema.new_session()
        answer = Answers.list_all_for_question(session, qid)
        schema.remove_session()
        return answer

    @staticmethod
    def questionHasAnswers(schema: Schema, qid: int) -> bool:

        session: Session = schema.new_session()
        answer = Answers.list_all_for_question(session, qid)
        size = len(answer)
        schema.remove_session()
        if size == 0:
            return False
        return True 