from fastapi import FastAPI
from .api import routes_posts, routes_titles
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Blog Title Generator + Mini CMS")

# Include routes
app.include_router(routes_posts.router, prefix="/api", tags=["posts"])
app.include_router(routes_titles.router, prefix="/api", tags=["titles"])

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_posts.router, prefix="/api/posts", tags=["posts"])
app.include_router(routes_titles.router, prefix="/api/titles", tags=["titles"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "blog-cms"}
