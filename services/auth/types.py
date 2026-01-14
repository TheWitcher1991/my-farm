from typing import TypedDict

from packages.kernel.types import JWTSignedSession
from users.types import UserRole


class LoginData(TypedDict):
    email: str
    password: str


class LoginSession(JWTSignedSession):
    role: UserRole
