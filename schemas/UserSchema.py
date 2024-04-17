from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    lastname: str
    type_user: str
    phone: str
    email: str
    username: str
    hash_password: str | None = None