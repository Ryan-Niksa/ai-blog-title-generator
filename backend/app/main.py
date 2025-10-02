from fastapi import FastAPI
from .api import routes_posts, routes_titles
from .database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Blog Title Generator + Mini CMS")

# Include routes
app.include_router(routes_posts.router, prefix="/api", tags=["posts"])
app.include_router(routes_titles.router, prefix="/api", tags=["titles"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "blog-cms"}
