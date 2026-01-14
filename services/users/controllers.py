from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase
from users.serializers import UserSerializer
from users.usecases import UserUseCase


class UserSetController(BaseSetController):
    prefix = "users"

    use_case = UserUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = UserSerializer
