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

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get ("id") == post_id:
            return post
    return {error:"Post not found"}
