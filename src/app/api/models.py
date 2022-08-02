from pydantic import BaseModel


class NoteSchema(BaseModel):
    title: str
    description: str


class NoteDB(BaseModel):
    id: int
