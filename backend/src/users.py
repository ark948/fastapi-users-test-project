import uuid
from typing import Optional

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users import FastAPIUsers, models
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

from src.db import User, get_user_db
from src.managers import UserManager
from src import config


SECRET = config.SECRET



async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="some-route/auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy[models.UP, models.ID]:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)



auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)



fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])



current_active_user = fastapi_users.current_user(active=True)