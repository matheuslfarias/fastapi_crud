from app.api import notes, ping
from fastapi import FastAPI
from app.db import engine, database, metadata


metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])

# To do - Routes

# /notes/ - GET - READ - GET ALL NOTES
# /notes/:id/ - GET - READ - GET A SINGLE NOTE
# /notes/ - POST - CREATE - ADD A NOTE
# /notes/:id/ - PUT - UPDATE - UPDATE A NOTE
# /notes/:id/ - DELETE - DELETE - DELETE A NOTE
