from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import items # Import your items router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def home():
    return {"message": "Welcome to the Item Blog API!"}

# Tell the main app to use the routes from items.py
app.include_router(items.router)