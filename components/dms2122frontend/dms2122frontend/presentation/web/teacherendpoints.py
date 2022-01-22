""" TeacherEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
from .webauth import WebAuth


class TeacherEndpoints():
    """ Monostate class responsible of handing the teacher web endpoint requests.
    """
    
    @staticmethod
    def get_teacher(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        return render_template('teacher.html', name=name, roles=session['roles'])

    @staticmethod
    def get_tStudents(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        return render_template('tStudents.html', name=name, roles=session['roles'])
    
    @staticmethod
    def get_tQuestions(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        arrayQuestions=[
            {"title": "Example Title 1", "desc": "Example description 1", "puntuation": 10, "penalization": -1, "c_right": 1, "c_1": "First Choice", "c_2": "Second Choice", "c_3": "Third Choice", "c_4": "Fourth Choice"},
            {"title": "Example Title 2", "desc": "Example description 2", "puntuation": 8, "penalization": -2, "c_right": 2, "c_1": "First Choice 2", "c_2": "Second Choice 2", "c_3": "Third Choice 2", "c_4": "Fourth Choice 2"},
            {"title": "Example Title 3", "desc": "Example description 3", "puntuation": 5, "penalization": 0, "c_right": 4, "c_1": "First Choice 3", "c_2": "Second Choice 3", "c_3": "Third Choice 3", "c_4": "Fourth Choice 3"}
        ]

        name = session['user']
        return render_template('tQuestions.html', name=name, roles=session['roles'], arrayQuestions=arrayQuestions)
    
    @staticmethod
    def get_tQuestionsCreate(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))

        afterSave = request.args.get('afterSave', default='/tQuestions')
        name = session['user']
        return render_template('tQuestionsCreate.html', name=name, roles=session['roles'], afterSave=afterSave)
    
    @staticmethod
    def get_tQuestionsModify(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        
        afterSave = request.args.get('afterSave', default='/tQuestions')
        name = session['user']
        return render_template('tQuestionsModify.html', name=name, roles=session['roles'], afterSave=afterSave,
            title="Example Title", desc="Example description",puntuation=10, penalization=-1, c_right=1, c_1="First Choice", c_2="Second Choice", c_3="Third Choice", c_4="Fourth Choice")
    
    @staticmethod
    def get_tQuestionsDisplay(auth_service: AuthService) -> Union[Response, Text]:
        # Redirect the user if it is not login or if he has not the right role
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.Teacher.name not in session['roles']:
            return redirect(url_for('get_home'))
        title: str = str(request.args.get('title'))
        afterSave = request.args.get('afterSave', default='/tQuestions')
        name = session['user']
        return render_template('tQuestionsDisplay.html', name=name, roles=session['roles'], afterSave=afterSave, title=title)