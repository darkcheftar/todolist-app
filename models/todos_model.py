from pydantic import BaseModel,Field

class Todo(BaseModel):
    title: str
    description: str
    status: str = Field(..., allowed_values=["To Do", "In Progress", "Done"])