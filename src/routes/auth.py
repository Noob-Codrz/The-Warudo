from fastapi import FastAPI, status, HTTPException, APIRouter, Depends
from fastapi.responses import RedirectResponse
from deps.dependencies import get_token_header


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Nott found"}},
    dependencies=[Depends(get_token_header)],
)

@router.get("/")
async def read_root():
    return {"Hello": "World"}

