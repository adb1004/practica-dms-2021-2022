from dms2122common.data.rest import ResponseData
from dms2122frontend.data.rest.backendservice import BackendService
from typing import Dict, List, Optional
from flask import session
from .webutils import WebUtils


class WebStatistics():
    @staticmethod
    def userStatistics(backend_service: BackendService, username: str) -> Optional[Dict]:
        rp: ResponseData = backend_service.userStatistics(session.get('token'), username)
        WebUtils.flash_response_messages(rp)
        return rp.get_content()

    @staticmethod
    def questionStatistics(backend_service: BackendService) -> Optional[Dict]:
        rp: ResponseData = backend_service.questionStatistics(session.get('token'))
        WebUtils.flash_response_messages(rp)
        if rp.get_content() is not None and isinstance(rp.get_content(), list):
            return list(rp.get_content())
        return [] 

    @staticmethod
    def usersStatistics(backend_service: BackendService) -> Optional[List[Dict]]:
        rp: ResponseData = backend_service.usersStatistics(session.get('token'))
        WebUtils.flash_response_messages(rp)
        if rp.get_content() is not None and isinstance(rp.get_content(), list):
            return list(rp.get_content())
        return []
