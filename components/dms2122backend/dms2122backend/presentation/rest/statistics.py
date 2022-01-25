from dms2122backend.service import StatisticsServices
from flask import current_app, session
from typing import List, Dict, Tuple, Union, Optional
from http import HTTPStatus

# Statistics from a particular user
def userStatistics(username: str) -> Tuple[Union[Dict, str], Optional[int]]:
    with current_app.app_context():
        try:
            uStatistics: Dict = StatisticsServices.userStatistics(
                username, current_app.db
                )
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (uStatistics, HTTPStatus.OK.value)

# Statistics from all the users
def usersStatistics() -> Tuple[Union[List[Dict], str], Optional[int]]:
    with current_app.app_context():
        try:
            uStatistics: List[Dict]  = StatisticsServices.usersStatistics(current_app.db)
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (uStatistics, HTTPStatus.OK.value) 

# Statistics from all the questions
def questionsStatistics() -> Tuple[Union[List[Dict], str], Optional[int]]:
    with current_app.app_context():
        try:
            sta: List[Dict]  = StatsServices.questionsStatistics(current_app.db)
        except ValueError: return ('An argument is missing', HTTPStatus.BAD_REQUEST.value)        
    return (sta, HTTPStatus.OK.value)