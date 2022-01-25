""" StudentEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, flash, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2122common.data import Role
from dms2122frontend.data.rest.backendservice import BackendService
from dms2122frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from .webquestion import WebQuestion
from .webanswer import WebAnswer
from .webstatistics import WebStatistics


class StudentEndpoints():
    """ Monostate class responsible of handling the student web endpoint requests.
    """
    @staticmethod
    def get_student(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the student root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('student.html', name=name, roles=session['roles'])

    @staticmethod
    def get_sProgression(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        return render_template('sProgression.html', name=name, roles=session['roles'], statistics=WebStatistics.userStatistics(backend_service, name))
    
    @staticmethod
    def get_sQuestions(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        return render_template('sQuestions.html', name=name, roles=session['roles'])
    
    @staticmethod
    def get_sQuestionsCompleted(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        return render_template('sQuestionsCompleted.html', name=name, roles=session['roles'], questions=WebQuestion.questionsCompletedFromUser(backend_service, name))
    
    @staticmethod
    def get_sQuestionsCompletedDisplay(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))

        qid:int = int(request.args.get('qid'))
        afterSave = request.args.get('afterSave', default='/sQuestions/Completed')
        name = session['user']
        return render_template('sQuestionsCompleted-Display.html', name=name, roles=session['roles'], afterSave=afterSave, question = WebQuestion.get_question(backend_service, qid), answer=WebAnswer.get_answer(backend_service, name, qid))
    
    @staticmethod
    def get_sQuestionsIncompleted(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))

        afterSave = request.args.get('afterSave', default='/student')
        name = session['user']
        return render_template('sQuestionsIncompleted.html', name=name, roles=session['roles'], arrayIncompleted=WebQuestion.questionsIncompletedFromUser(backend_service, name))
    
    @staticmethod
    def get_sQuestionsIncompletedComplete(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))
        qid: int = str(request.args.get('qid'))
        afterSave = request.args.get('afterSave', default='/sQuestions/Incompleted')
        name = session['user']
        return render_template('sQuestionsIncompleted-Complete.html', name=name, roles=session['roles'], afterSave=afterSave, question = WebQuestion.get_question(backend_service ,qid))
    
    @staticmethod
    def post_sQuestionsIncompletedComplete(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Student.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        number = 0

        c = str(request.form['choices'])
        if c == 'c_1': number = 1
        elif c == 'c_2': number = 2
        elif c == 'c_3': number = 3
        elif c == 'c_4': number = 4

        nAnswer = WebAnswer.answer_question(backend_service, int(request.form['qid']), number, str(name))
        if not nAnswer: return redirect(url_for('get_sQuestionsIncompleted'))

        afterSave = url_for('get_sQuestionsIncompleted')

        return redirect(afterSave)