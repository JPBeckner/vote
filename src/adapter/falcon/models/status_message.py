from pydantic import BaseModel, Field


class StatusMessage(BaseModel):
    message: str = Field(
        title="Message",
        description="The response description message",
    )
    status: str = Field(
        title="Status",
        description="The response http status"
    )