import uuid

from fastapi import FastAPI

from models.course import Course
from models.player import Player



app = FastAPI()


players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

@app.get("/players")
async def get_player():
    pass

@app.post("/players")
async def new_player():
    pass

@app.delete("/players{player_id}")
async def del_player(player_id):
    pass

@app.put("/players{player_id}")
async def update_player(player_id):
    pass

@app.get("/courses")
async def get_course():
    pass

@app.post("/courses")
async def new_course():
    pass

@app.put("/courses{course_id}")
async def update_course(course_id):
    pass

@app.delete("/courses{course_id}")
async def del_course(course_id):
    pass
