from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date, time
from enum import Enum
from typing import List

app = FastAPI()

class NotificationMethod(str, Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"

class ReminderCreate(BaseModel):
    date: date
    time: time
    message: str
    notification_method: NotificationMethod

class Reminder(ReminderCreate):
    id: int

# In-memory database
reminders_db: List[dict] = []
current_id = 1

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Remind-me-later API",
        "endpoints": {
            "create_reminder": "POST /reminders/",
            "get_reminder": "GET /reminders/{id}"
        }
    }

# Create reminder
@app.post("/reminders/", response_model=Reminder, status_code=201)
async def create_reminder(reminder: ReminderCreate):
    global current_id
    reminder_data = reminder.dict()
    reminder_data["id"] = current_id
    reminders_db.append(reminder_data)
    current_id += 1
    return reminder_data

# Get reminder
@app.get("/reminders/{reminder_id}", response_model=Reminder)
async def read_reminder(reminder_id: int):
    for reminder in reminders_db:
        if reminder["id"] == reminder_id:
            return reminder
    raise HTTPException(status_code=404, detail="Reminder not found")

# List all reminders
@app.get("/reminders/", response_model=List[Reminder])
async def list_reminders():
    return reminders_db