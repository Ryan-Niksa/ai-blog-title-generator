from fastapi import FastAPI
from .api import routes_posts
from .database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Blog Title Generator + Mini CMS")

# Routes
app.include_router(routes_posts.router, prefix="/api", tags=["posts"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "blog-cms"}
