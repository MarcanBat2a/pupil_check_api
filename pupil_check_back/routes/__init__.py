"""Routes for the FastAPI application."""

from fastapi import APIRouter
from pupil_check_back.routes.video import video_router

router = APIRouter()
router.include_router(video_router)
