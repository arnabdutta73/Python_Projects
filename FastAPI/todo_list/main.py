from fastapi import FastAPI
from database import Base, engine
from routes import tasks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(tasks.router, prefix="/tasks")

# Run the app
# uvicorn main:app --reload
