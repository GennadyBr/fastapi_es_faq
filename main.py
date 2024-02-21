import os
from logging import getLogger

import uvicorn
from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from api.v1.delete_router import delete_router
from api.v1.get_all_router import get_all_router
from api.v1.register_router import register_router
from api.v1.search_router import search_router
from api.v1.update_router import update_router
from config.logging_setup import LoggerSetup

logger_setup = LoggerSetup()
LOGGER = getLogger(__name__)
load_dotenv()

app = FastAPI(
    debug=True,
    version="0.0.1",
    docs_url="/docs",
    openapi_url="/openapi.json",
    title="FastAPI - ElasticSearch API",
)


# Обработка ошибок HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)


# Middleware для логирования запросов
@app.middleware("http")
async def log_requests(request: Request, call_next):
    LOGGER.info(f"REQUEST METHOD {request.method} {request.url}")
    response = await call_next(request)
    return response


# Middleware для CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

main_api_router = APIRouter()

#     1. Добавление вопросов и ответов в базу данных ElasticSearch.
main_api_router.include_router(register_router, prefix="/register", tags=["register"])

#     2. Изменение вопросов и ответов в базу данных ElasticSearch.
main_api_router.include_router(update_router, prefix="/update", tags=["update"])

#     3. Удаление вопросов и ответов в базу данных ElasticSearch.
main_api_router.include_router(delete_router, prefix="/delete", tags=["delete"])

#     4. Полнотекстовый поиск вопросов в базе данных ElasticSearch.
main_api_router.include_router(search_router, prefix="/search", tags=["search"])

#     5. Все данные из базы
main_api_router.include_router(get_all_router, prefix="/get_all", tags=["get_all"])

app.include_router(main_api_router)


@app.on_event("startup")
async def startup_event():
    LOGGER.info("--- Start up App ---")


@app.on_event("shutdown")
async def shutdown():
    LOGGER.info("--- Shutdown App ---")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APP_PORT")))
