from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI() 


posts: list[dict] = [
    {"title": "First Post", "content": "This is the content of the first post."},
    {"title": "Second Post", "content": "This is the content of the second post."}
]

@app.get("/", response_class= HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]["content"]}<h1>"
@app.get("/api/posts")
def get_posts():
    return posts