from django.db import transaction

from auth.types import LoginData, LoginSession
from packages.framework.contrib import authenticate
from packages.kernel.types import ExtendedRequest, JWTRefreshSession
from packages.usecases.jwt import jwt_use_case
from users.types import CreateUserData, CreateUserDTO


class AuthUseCase:
    def refresh(self, request: ExtendedRequest) -> JWTRefreshSession:
        return jwt_use_case.refresh(request.user)

    @transaction.atomic
    def login(self, request: ExtendedRequest, data: LoginData) -> LoginSession:

        user = authenticate(
            request=request,
            email=data["email"],
            password=data["password"],
        )

        session = jwt_use_case.sign(user)

        session["user"] = user.id
        session["role"] = user.role

        return session

    @transaction.atomic
    def register(self, data: CreateUserData) -> CreateUserData:
        dto = CreateUserDTO(**data)

        return data


auth_use_case = AuthUseCase()
