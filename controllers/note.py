from config.db import conn
from schemas.note import noteEntity, notesEntity

def get_all_notes():
    try:
        docs = list(conn.fastapiTest.notes.find({}))
        print(docs)
        notes = notesEntity(docs)
        return notes
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": "An unexpected error occurred"}

def create_note(note):
  result = conn.fastapiTest.notes.insert_one(dict(note))
  inserted_id = result.inserted_id
  return noteEntity(conn.fastapiTest.notes.find_one({"_id": inserted_id}))