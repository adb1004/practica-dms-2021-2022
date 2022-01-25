from dms2122backend.logic.logicanswer import LogicAnswer
from dms2122backend.logic.logicquestion import LogicQuestion
from dms2122backend.data.db.resultsets import Answers
from dms2122backend.data.db.results import Answer, Question
from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session

# Class that manages the logic behind the statistics
class LogicStatistics():

    # Totality of all the questions puntuation
    @staticmethod
    def totalQuestionsPuntuation(session: Session)->float:
        questions : List[List] = LogicQuestion.questionsList(session)
        score : float = 0
        
        for q in questions:
            q2: Question = q[0]
            score= score + q2.puntuation
        
        return score

    # Statistics from a user
    @staticmethod
    def userStatistics(session: Session, user: str)-> Dict:
        statistics: Dict = {}
        try:
            answerList : List[Answer] = Answers.answerListFromUser(session,user)

            completedQScore:float=0
            scoreCompleted:float=0
            totalScore:float=0
            uScore:float = 0

            p: Optional[float] = 0
            nAnswers: int = len(answerList)
            
            for a in answerList:
                question: Question = LogicQuestion.getQuestionFromId(session, a.qid)
                if question is not None:
                    p = LogicAnswer.answerScore(session,a)
                    
                    if p is not None:  uScore = uScore + p
                    
                    completedQScore = completedQScore + question.puntuation

            totalScore = uScore / LogicStatistics.totalQuestionsPuntuation(session) * 10
            scoreCompleted = uScore / completedQScore * 10
            
            statistics['nAnswers'] = nAnswers
            statistics['uScore'] = uScore
            statistics['scoreCompleted'] = scoreCompleted
            statistics['totalScore'] = totalScore
            
            return statistics
        except Exception as exception: raise exception

    # Statistics from all the users
    @staticmethod
    def usersStatistics(session: Session) -> List[Dict]:
        try:
            v: List = []
            answers : List[Answer]= LogicAnswer.allAnswers(session)
            users:List=[]

            for a in answers:
                user : str = a.user
                
                if not user in users:
                    users.append(user)

            for user in users:
                dic : Dict = LogicStatistics.userStatistics(session, user)
                v.append(dic)

            return v
        except Exception as exception: raise exception

    # All the statistics from all the questions
    @staticmethod
    def questionsStatistics(session: Session)-> List[Dict]:
        try:
            questions : List[Question] = LogicQuestion.questionsList(session)
            v: List = []
            
            for q in questions:
                q2 : Question = q[0]
                answers: List[Answer] = LogicAnswer.answerListFromQuestion(session, q2.qid)
                n_answers = len(answers)
                d: Dict={}
                
                if 0 < n_answers:
                    n_c1 : int = 0
                    n_c2 : int = 0
                    n_c3 : int = 0
                    n_c4 : int = 0

                    p: Optional[float] = 0
                    avg:float=0
                    qp : float = 0
                    
                    for a in answers:
                        choice : int = a.id
                        
                        if choice == 1: n_c1 = n_c1 + 1
                        elif choice == 2: n_c2 = n_c2 + 1
                        elif choice == 3: n_c3 = n_c3 + 1
                        else: n_c4 = n_c4 + 1
                        
                        p = LogicAnswer.answerScore(session, a)
                        if p is not None: qp = qp + p
                    
                    d['title']=q2.title
                    d['n_answers'] = n_answers
                    d['n_c1'] = n_c1
                    d['n_c2'] = n_c2
                    d['n_c3'] = n_c3
                    d['n_c4'] = n_c4
                    d['avg']= qp / n_answers

                    v.append(d)
                else:
                    d['title']=q2.title
                    d['n_answers'] = 0
                    d['n_c1'] = 0
                    d['n_c2'] = 0
                    d['n_c3'] = 0
                    d['n_c4'] = 0
                    d['avg'] = 0

                    v.append(d)
            return v   
        except Exception as exception: raise exception
        