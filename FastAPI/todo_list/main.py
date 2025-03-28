from fastapi import FastAPI
from database import Base, engine
from routes import tasks

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(tasks.router, prefix="/tasks")

# Run the app
# uvicorn main:app --reload
