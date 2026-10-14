from pydantic import BaseModel

class User(BaseModel):
    name : str
    age : int
    email : str

#valid data
user= User(name="Rafia", age=23, email="rafia@gmail.com")
print(user)

#invalid user
try:
    invalid_user = User(name="Alice", age="thirty", email="alice@gmail.com")
except ValueError as e:
    print(e)