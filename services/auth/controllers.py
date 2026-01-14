from auth.usecases import AuthUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class AuthSetController(BaseSetController):
    prefix = "auth"

    use_case = AuthUseCase()
    serializer_use_case = SerializerUseCase()
