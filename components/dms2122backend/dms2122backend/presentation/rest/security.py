from dms2122auth.service import UserServices
from dms2122auth.data.config import AuthConfiguration
from typing import Dict, Optional
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer
from connexion.exceptions import Unauthorized


def verify_api_key(token: str) -> Dict:
    with current_app.app_context():
        cfg: AuthConfiguration = current_app.cfg
        if not token in cfg.get_authorized_api_keys():
            raise Unauthorized('API key not valid')
    return {}