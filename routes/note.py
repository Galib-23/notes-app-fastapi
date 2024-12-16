from fastapi import APIRouter, FastAPI, Request
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity


note = APIRouter()

@note.get("/")
async def read_item(request: Request):
    try:
        docs = list(conn.fastapiTest.notes.find({}))
        print(docs)
        notes = notesEntity(docs)
        return notes
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": "An unexpected error occurred"}

  
@note.post("/")
async def add_note(note: Note):
  result = conn.fastapiTest.notes.insert_one(dict(note))
  inserted_id = result.inserted_id
  inserted_note = conn.fastapiTest.notes.find_one({"_id": inserted_id})
  return noteEntity(inserted_note)