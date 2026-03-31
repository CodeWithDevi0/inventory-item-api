# Item Inventory API

*A simple FastAPI and MySQL backend I built to learn how systems communicate.*

## What I Learned in this Project
Instead of putting all my code in one massive file, I learned how to organize a project professionally by separating the logic:

- **Routers (`routers/`):** I learned how to use `APIRouter` to cleanly handle API endpoints (like `GET` and `POST`) without mixing them with database code.
- **Services (`services/`):** I learned to put my actual SQL queries and logic in separate files. This makes the main code much easier to read and fix.
- **Pydantic Models:** I learned how to use `BaseModel` to automatically check the data coming from the frontend (like making sure `price` is actually a number before saving it).
- **Database Connection:** I learned how to connect Python to MySQL safely. I also learned to use `%s` placeholders to prevent SQL injection, and how to use `conn.commit()` to properly save new data.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** MySQL (XAMPP)
- **CORS:** Pre-configured so my future Vue.js frontend can easily connect to it.

## Current Features
- `GET /api/items` — Fetch all items from the database.
- `GET /api/items/{id}` — Fetch one specific item using Path Parameters.
- `POST /api/items` — Add a new item to the database.
*(PUT and DELETE endpoints are next!)*