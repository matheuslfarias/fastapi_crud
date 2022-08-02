from pydoc import describe
from fastapi import Query
from app.api.models import NoteSchema
from app.db import notes, database


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, descriptions=payload.descriptions)
    return await database.execute(query=query)
