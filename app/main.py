from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = "CI/CD Notes API")

notes = []

class Note(BaseModel):
    text: str



@app.get("/")
def root():
    return {"message": "CI/CD Notes API"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/notes")
def get_notes():
    return {"notes": notes}

@app.post("/notes")
def create_notes(note: Note):
    notes.append(note.text)
    return {"created": note.text}