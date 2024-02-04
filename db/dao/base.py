from __future__ import annotations

from typing import Generic, List, Optional, Type, TypeVar

from tortoise.models import Model
from tortoise.queryset import QuerySet

MODEL_TYPE = TypeVar("MODEL_TYPE", bound=Model)


class BaseDAO(Generic[MODEL_TYPE]):
    _model: MODEL_TYPE
    default_prefetch_related: Optional[List[str]] = None

    async def get_by_id(self, pk: int, prefetch_related=[]) -> Type[MODEL_TYPE]:
        if self.default_prefetch_related:
            prefetch_related = self.default_prefetch_related
        return await self._model.get(pk=pk).prefetch_related(*prefetch_related)

    def get_by_id_queryset(self, pk: int) -> Type[MODEL_TYPE]:
        return self._model.get(pk=pk)

    async def get_by_id_or_none(self, pk: int) -> Type[MODEL_TYPE]:
        return await self._model.get_or_none(pk=pk)

    async def update(self, pk, data) -> Type[MODEL_TYPE]:
        instance = await self.get_by_id(pk)
        for k, v in data.items():
            if v is not None:
                setattr(instance, k, v)
        await instance.save()
        return instance

    async def create(self, **kwargs) -> Type[MODEL_TYPE]:
        return await self._model.create(**kwargs)

    async def get_list(self) -> List[MODEL_TYPE]:
        return await self._model.all()

    async def list(self) -> QuerySet:
        return self._model.all()

    async def filter(self, first=False, **filters) -> QuerySet:
        queryset = self._model.filter(**filters)

        if first:
            queryset = queryset.first()

        return await queryset

    async def delete(self, pk: int = None, instance: MODEL_TYPE = None) -> None:
        if instance:
            await instance.delete()
            return
        instance = await self.get_by_id(pk)
        await instance.delete()
