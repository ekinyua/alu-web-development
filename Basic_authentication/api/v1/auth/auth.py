#!/usr/bin/env python3
"""Authentication Module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """validate if endpoint requires authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] == '*':
                if exc[:l_exc - 1] in tmp_path:
                    return False
            else:
                if exc == tmp_path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """validate authorization header"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """validate current user"""
        return None
