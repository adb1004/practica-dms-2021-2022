from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer
from typing import Dict, Optional, Tuple
from http import HTTPStatus


def health_test() -> Tuple[None, Optional[int]]:
    return (None, HTTPStatus.NO_CONTENT.value) 