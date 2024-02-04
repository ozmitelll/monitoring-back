import bcrypt
from fastapi import APIRouter, HTTPException

from models.app_models import UserModel, UserDTO

auth = APIRouter()
router = APIRouter()


@auth.post('/login')
async def login(username: str, password: str):
    user = await UserModel.get(username=username)
    if password == user.password:
        return {"user": user}
    else:
        raise HTTPException(status_code=400, detail="Incorrect credentials")


@auth.post('/register', response_model=None)
async def register(request: UserDTO):
    if await UserModel.filter(username=request.username).exists():
        raise HTTPException(status_code=400, detail="Username is already exists!")

    await UserModel.create(
        username=request.username,
        password=request.password,
        name=request.name,
        surname=request.surname,
        thirdname=request.thirdname,
        unit=request.unit,
        role_id=request.role_id,
        rank_id=request.rank_id
    )

    return {"message": "User registered successfully"}


