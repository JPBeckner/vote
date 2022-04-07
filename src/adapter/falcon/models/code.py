from pydantic import BaseModel, Field


class Code(BaseModel):
    code: int = Field(
        title="code",
        description="Vote option Code",
    )