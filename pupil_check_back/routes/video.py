from dependency_injector.wiring import inject
from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/save", status_code=201)
@inject
async def save():
    """Save a video."""
    try:
        pass
    except Exception as ex:
        print(str(ex), True)

    return {"message": "Video saved successfully."}
