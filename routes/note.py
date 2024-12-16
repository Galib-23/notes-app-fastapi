from fastapi import APIRouter, FastAPI, Request
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from controllers.note import get_all_notes, create_note


note = APIRouter()

@note.get("/")
async def read_notes():
  return get_all_notes()
  
@note.post("/")
async def add_note(note: Note):
  return create_note(note)