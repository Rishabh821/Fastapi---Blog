from fastapi import FastAPI ,Request
from fastapi.templating import Jinja2Templates
app = FastAPI() 

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {"title": "First Post", "content": "This is the content of the first post."},
    {"title": "Second Post", "content": "This is the content of the second post."},
    {"title":"Home", "content":"fcuk you"}
]

@app.get("/", include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title": "Home"})
    
@app.get("/api/posts")
def get_posts():
    return posts