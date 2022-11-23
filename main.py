from typing import Optional,List
from fastapi import FastAPI
from pydantic import BaseModel

class Participants(BaseModel):
    email:str
    is_active:bool
    bio:Optional[str]


app = FastAPI()

participants=[]


@app.get("/participants",response_model=List[Participants])
async def get_participants():
    return participants
    

@app.post("/register")
async def register_participants(participant:Participants):
    participants.append(participant)

@app.get("/participants/{id}")
async def get_participant_by_id(id:int):
    return participants[id]










