# Item Inventory API

*A simple FastAPI and MySQL backend I built to learn how systems communicate.*

## What I Learned in this Project
Instead of putting all my code in one massive file, I learned how to organize a project professionally by separating the logic:

- **Routers (`routers/`):** I learned how to use `APIRouter` to cleanly handle API endpoints (`GET`, `POST`, `PUT`, and `DELETE`) without mixing them with database code.
- **Services (`services/`):** I learned to put my actual SQL queries and logic in separate files. This makes the main code much easier to read and fix.
- **The DRY Principle (Helper Functions):** I learned how to refactor repetitive database connection code into dynamic helper functions (`execute_read_query` and `execute_write_query`).
- **Professional Error Handling:** I implemented `try-except` blocks and learned to use FastAPI's `HTTPException` to gracefully catch database errors and return standard 404 or 500 status codes.
- **Pydantic Models:** I learned how to use `BaseModel` to automatically check the data coming from the frontend (like making sure `price` is actually a number before saving it).
- **Database Connection & Python Quirks:** I learned how to connect Python to MySQL safely, use `%s` placeholders to prevent SQL injection, and navigate Python's "Tuple Trap" by using trailing commas for single variables `(item_id,)`.
- **Variable Shadowing:** I learned how assigning new data to an existing variable name overwrites it, and how to use the underscore (`_`) as a "trash can" variable to safely discard unneeded return values.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** MySQL (XAMPP)
- **CORS:** Pre-configured so my future Vue.js frontend can easily connect to it.

## Current Features (Full CRUD Complete)
- `GET /api/items` — Fetch all items from the database.
- `GET /api/items/{id}` — Fetch one specific item using Path Parameters.
- `POST /api/items` — Add a new item to the database.
- `PUT /api/items/{id}` — Update an existing item's details.
- `DELETE /api/items/{id}` — Remove an item from the database.