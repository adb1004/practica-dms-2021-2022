from dms2122backend.data.config import BackendConfiguration
from typing import Dict, Optional
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer
from connexion.exceptions import Unauthorized


def verify_api_key(token: str) -> Dict:
    with current_app.app_context():
        cfg: BackendConfiguration = current_app.cfg
        if not token in cfg.get_authorized_api_keys():
            raise Unauthorized('API key not valid')
    return {}