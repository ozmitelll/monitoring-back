from models.app_models import (
    UserModel,
)

from .base import BaseDAO

class UserDAO:
    async def get_by_id(self, pk: int) -> UserModel:
        return await UserModel.get(id=pk)

    async def update(self, data: dict, pk: int = None, instance: UserModel = None):
        if pk:
            instance = await self.get_by_id(pk)

        for k, v in data.items():
            if v:
                setattr(instance, k, v)
        await instance.save()