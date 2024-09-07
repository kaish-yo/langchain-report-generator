import logging

from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware

from app.api.v1 import healthcheck
from app.core.config import get_settings
from app.core.logger.custom_logging import logger as custom_logger


# loggingセットアップ
class NoParsingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.getMessage().find("/docs") >= 0


# 環境変数など
settings = get_settings()


# init FastAPI
def create_app() -> FastAPI:
    app = FastAPI(
        title=f"[{settings.ENV}]{settings.TITLE}",
        version=settings.VERSION,
        debug=settings.DEBUG or False,
        # root_path=f"{settings.API_GATEWAY_STAGE_PATH}/",
    )
    app.logger = custom_logger
    return app


app = create_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
    allow_origin_regex=r"^https?:\/\/([\w\-\_]{1,}\.|)example\.com",
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["info"])
def get_info(request: Request, response: Response) -> dict[str, str]:
    logger = request.app.logger
    logger.debug("The DEBUG mode is turned on.")
    return {"title": settings.TITLE, "version": settings.VERSION}


app.include_router(healthcheck.router)
