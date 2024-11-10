from fastapi import APIRouter, Depends
from src.users import fastapi_users, auth_backend
from src.users import current_active_user
from src.schemas import UserCreate, UserRead, UserUpdate
from src.models import User



auth_router = APIRouter(
    prefix='/some-route'
)


auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend), 
    prefix="/auth/jwt", tags=["auth"]
)
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)




@auth_router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}