from fastapi import APIRouter

from app.core.logger.custom_logging import logger

router = APIRouter(tags=["healthcheck"], prefix="/api/v1")


@router.get("/healthcheck", tags=["healthcheck"])
def check_health():
    logger.info("healthcheck")
    return {"message": "OK"}
