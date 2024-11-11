import uuid

from fastapi_users import FastAPIUsers, models
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from src.apps.auth.managers import get_user_manager
from src.apps.auth.config import SECRET
from src.apps.auth.models import User



bearer_transport = BearerTransport(tokenUrl="user-manager/auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy[models.UP, models.ID]:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)



auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)



fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])



current_active_user = fastapi_users.current_user(active=True)