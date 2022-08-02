from app.api import ping
from fastapi import FastAPI

app = FastAPI()


app.include_router(ping.router)


# To do - Routes

# /notes/ - GET - READ - GET ALL NOTES
# /notes/:id/ - GET - READ - GET A SINGLE NOTE
# /notes/ - POST - CREATE - ADD A NOTE
# /notes/:id/ - PUT - UPDATE - UPDATE A NOTE
# /notes/:id/ - DELETE - DELETE - DELETE A NOTE
