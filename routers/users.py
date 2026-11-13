from fastapi import Depends, APIRouter
from security import oauth2_scheme
from deps import get_current_user
from models import User

router = APIRouter(tags=["users"])

@router.get("/items")
async def get_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@router.get("/users/profile")
async def get_users_profile(current_user: User = Depends(get_current_user)):
    return current_user