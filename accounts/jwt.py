
from rest_framework_simplejwt.tokens import RefreshToken as JWTRefreshToken

from accounts.models.base_user import User


def get_user_jwt_token(user: User) -> tuple[str, str]:
    refresh_object = JWTRefreshToken.for_user(user)
    return str(refresh_object.access_token), str(refresh_object)
