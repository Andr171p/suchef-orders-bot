from pydantic import BaseModel, field_validator
import re


class UserSchema(BaseModel):
    user_id: int
    username: str | None
    phone: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        pattern = r'\+\d$\d{3}$\d{3}-\d{2}-\d{2}'
        if bool(re.fullmatch(pattern, value)):
            raise ValueError("Invalid phone format")
        return value
