from pydantic import BaseModel, Field

class CreateTask(BaseModel):
    title:str = Field(min_length = 1)
    done:bool = True

class UpdateTaskStatus(BaseModel):
    done:bool = True