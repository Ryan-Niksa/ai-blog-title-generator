# AI Blog Title Generator & Mini CMS

This project is a **full-stack web application** that demonstrates AI-powered blog title generation and simple content management. It’s built using **FastAPI** (backend), **SQLite + SQLAlchemy** (database), **OpenAI API** (AI title generation), and **React (Vite)** (frontend).

---

## Features

* **AI Blog Title Generator**

  * Enter a topic → get AI-suggested blog titles using OpenAI.
  * Choose and use a title directly in the post editor.

* **Mini CMS for Blog Posts**

  * Create, list, and delete blog posts.
  * Simple and clean UI for managing content.

* **Modern Frontend**

  * Built with React (Vite) and Axios.
  * Styled with lightweight CSS (no Tailwind).

* **Backend API**

  * FastAPI REST API with `/api/titles` and `/api/posts` endpoints.
  * CORS enabled for frontend-backend communication.
  * Modular structure with routers, services, schemas, and models.

---

## Project Structure

```
Blog_Title_Generator/
│
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── api/           # API routes
│   │   ├── services/      # Business logic (AI calls)
│   │   ├── models.py      # SQLAlchemy models
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── crud.py        # Database operations
│   │   ├── database.py    # DB connection
│   │   ├── config.py      # Settings (dotenv)
│   │   └── main.py        # FastAPI entrypoint
│   ├── venv/              # Virtual environment
│   └── requirements.txt   # Python dependencies
│
├── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # UI components
│   │   ├── api.js         # Axios API client
│   │   ├── App.jsx        # Main app
│   │   └── App.css        # Global styles
│   ├── index.html         # Entry point
│   ├── package.json       # NPM dependencies
│   └── vite.config.js     # Vite config
│
└── README.md              # Documentation (this file)
```

---

## Backend Setup

1. Navigate to backend folder:

   ```bash
   cd backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   venv/scripts/activate   # Windows
   source venv/bin/activate # macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   DATABASE_URL=sqlite:///./blog.db
   ```

5. Run the backend:

   ```bash
   uvicorn app.main:app --reload
   ```

6. Open API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Frontend Setup

1. Navigate to frontend folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```

4. Open frontend at: [http://localhost:5173](http://localhost:5173)

---

## API Endpoints

### Titles

* `GET /api/titles/` → Generate AI titles

  * Params: `topic` (str), `n` (int, default=5)

### Posts

* `POST /api/posts/` → Create new post
* `GET /api/posts/` → Fetch all posts
* `PUT /api/posts/{id}` → Update post
* `DELETE /api/posts/{id}` → Delete post

---

## Example Workflow

1. Enter a topic in **AI Blog Title Generator**.
2. Get 5 AI-suggested blog titles.
3. Click **Use** to auto-fill into **Create Blog Post** form.
4. Add content and save post.
5. Manage posts in **All Blog Posts** section.

---

## Tech Stack

* **Backend:** FastAPI, SQLAlchemy, Pydantic, Uvicorn, python-dotenv
* **Frontend:** React (Vite), Axios
* **Database:** SQLite
* **AI:** OpenAI API

---
## Known Issues / Improvements

* Requires valid OpenAI API key.
* No authentication (public CMS for now).
* Posts stored in SQLite (consider Postgres for production).
* Titles are generated on-demand only.

---

## License

MIT License. Free to use and modify.

---