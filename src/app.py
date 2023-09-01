from routes.routes import router as main_router

from fastapi import FastAPI, Depends, HTTPException, status

app  = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World_app.py"}

app.include_router(main_router)

