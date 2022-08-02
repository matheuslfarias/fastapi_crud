from pydoc import describe
from fastapi import Query
from app.api.models import NoteSchema
from app.db import notes, database


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    query = notes.select().where(title=id == notes.c.id)
    return await database.fetch_onde(query=query)
