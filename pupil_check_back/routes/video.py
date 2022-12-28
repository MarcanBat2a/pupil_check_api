import os

import aiofiles
from fastapi import APIRouter, File, UploadFile

video_router = APIRouter(prefix="/videos", tags=["Videos"])


@video_router.post("/save", status_code=201)
async def save(video: UploadFile = File(...)):
    """Save a video."""
    try:
        end_file = str(len(os.listdir("pupil_check_back/video_saved")) + 1)
        async with aiofiles.open(f"pupil_check_back/video_saved/video_{end_file}.mp4", "wb") as out_file:
            content = await video.read()
            await out_file.write(content)

        return {"Result": "OK"}
    except Exception as ex:
        print(str(ex), True)
        return {"message": "Video saved successfully."}
