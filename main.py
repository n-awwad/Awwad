from fastapi import FastAPI
import fastapi
app=FastAPI() 

@app.post("/CreatePost")
async def create_posts():
    return {"Message": "Successfully Create Post"}

@app.get("/")
async  def root():
    return {"message": "Maitre'D Integration"}

@app.get("/posts")
async def getpost():
 return {"Data": "this is your post"}

