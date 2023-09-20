from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
from routes.auth import router as auth_router

router = APIRouter()

