from typing import TypedDict
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


# mypy проверяет статически, pydantic при выполнении
# поэтому для mypy используем TypedDict
class UserData(TypedDict, total=False):
    id: int
    username: str
    email: str
    is_active: bool


user_data: UserData = {"id": 1, "username": "Agapit", "email": "aga@supermail"}

# mypy проверяет статически, pydantic при выполнении
user1 = User(**user_data)

print(user1)
print(user1.username, user1.is_active)
print()

user_data2 = {"id": 2, "username": "Foma", "email": "foma@mail", "is_active": False}
user2 = User(**user_data2)  # mypy не может проверить типы и выдаёт предупреждение. Выполняется нормально
print(user2)
print(user2.username, user2.is_active)
print()

user3 = User(id=3, username="As", email="as@mail")
print(user3)
print(user3.username, user3.is_active)
print()


user_data4 = {"id": "three", "username": "Egor", "email": "egor@ya"}
user4 = User(**user_data4)  # mypy не может проверить типы и выдаёт предупреждение. Ошибка при выполнении
print(user4)
print(user4.username, user4.is_active)
print()
