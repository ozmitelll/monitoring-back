from tortoise import Model, fields
from pydantic import BaseModel

class RankModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)

    class Meta:
        table = "ranks"

class RoleModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)

    class Meta:
        table = "roles"

class UserModel(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password = fields.CharField(max_length=255)
    name = fields.CharField(max_length=50)
    surname = fields.CharField(max_length=50)
    thirdname = fields.CharField(max_length=50, null=True)
    rank = fields.ForeignKeyField("models.RankModel", related_name="users")
    unit = fields.CharField(max_length=50)
    role = fields.ForeignKeyField("models.RoleModel", related_name="users")

    class Meta:
        table = "users"


class UserDTO(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    thirdname: str
    unit: str
    role_id: int
    rank_id: int
