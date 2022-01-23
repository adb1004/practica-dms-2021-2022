""" StudentEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from .webquestion import WebQuestion
from .webanswer import WebAnswer


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
    def get_sProgression(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        return render_template('sProgression.html', name=name, roles=session['roles'])
    
    @staticmethod
    def get_sQuestions(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        return render_template('sQuestions.html', name=name, roles=session['roles'])
    
    @staticmethod
    def get_sQuestionsCompleted(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        arrayCompleted=[
            {"title": "Example Title 1", "desc": "Example description 1", "puntuation": 10, "penalization": -1, "c_right": 1, "c_1": "First Choice", "c_2": "Second Choice", "c_3": "Third Choice", "c_4": "Fourth Choice"},
            {"title": "Example Title 2", "desc": "Example description 2", "puntuation": 8, "penalization": -2, "c_right": 2, "c_1": "First Choice 2", "c_2": "Second Choice 2", "c_3": "Third Choice 2", "c_4": "Fourth Choice 2"},
            {"title": "Example Title 3", "desc": "Example description 3", "puntuation": 5, "penalization": 0, "c_right": 4, "c_1": "First Choice 3", "c_2": "Second Choice 3", "c_3": "Third Choice 3", "c_4": "Fourth Choice 3"}
        ]

        name = session['user']
        return render_template('sQuestionsCompleted.html', name=name, roles=session['roles'], arrayCompleted=arrayCompleted)
    
    @staticmethod
    def get_sQuestionsCompletedDisplay(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        title: str = str(request.args.get('title'))
        afterSave = request.args.get('afterSave', default='/sQuestions/Completed')
        name = session['user']
        return render_template('sQuestionsCompleted-Display.html', name=name, roles=session['roles'], afterSave=afterSave, title=title)
    
    @staticmethod
    def get_sQuestionsIncompleted(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        arrayIncompleted=[
            {"title": "Example Title 1", "desc": "Example description 1", "puntuation": 10, "penalization": -1, "c_right": 1, "c_1": "First Choice", "c_2": "Second Choice", "c_3": "Third Choice", "c_4": "Fourth Choice"},
            {"title": "Example Title 2", "desc": "Example description 2", "puntuation": 8, "penalization": -2, "c_right": 2, "c_1": "First Choice 2", "c_2": "Second Choice 2", "c_3": "Third Choice 2", "c_4": "Fourth Choice 2"},
            {"title": "Example Title 3", "desc": "Example description 3", "puntuation": 5, "penalization": 0, "c_right": 4, "c_1": "First Choice 3", "c_2": "Second Choice 3", "c_3": "Third Choice 3", "c_4": "Fourth Choice 3"}
        ]
        afterSave = request.args.get('afterSave', default='/student')
        name = session['user']
        return render_template('sQuestionsIncompleted.html', name=name, roles=session['roles'], arrayIncompleted=arrayIncompleted)
    
    @staticmethod
    def get_sQuestionsIncompletedComplete(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        title: str = str(request.args.get('title'))
        afterSave = request.args.get('afterSave', default='/sQuestions/Incompleted')
        name = session['user']
        return render_template('sQuestionsIncompleted-Complete.html', name=name, roles=session['roles'], afterSave=afterSave, title=title)
    
    @staticmethod
    def post_sQuestionsIncompletedComplete(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        afterSave = request.args.get('afterSave', default='/sQuestions/Incompleted')
        return redirect(afterSave)